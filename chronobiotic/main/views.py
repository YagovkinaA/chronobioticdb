from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Chronobiotic, PublicationRecord, ChatLog
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, EmailMessage
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.conf import settings
from django_ratelimit.decorators import ratelimit
from .utills import  get_agent_url
import requests
import csv, io



def index(request):
    query = request.GET.get('search', '')
    model = Chronobiotic.objects.all().prefetch_related(
        'effect',
        'target',
        'mechanisms',
        'articles',
        'synonyms'  # Добавляем предзагрузку синонимов
    )

    if query:
        model = model.filter(
            Q(gname__icontains=query) |
            Q(molecula__icontains=query) |
            Q(fdastatus__icontains=query) |
            Q(smiles__icontains=query) |
            Q(effect__Effectname__icontains=query) |
            Q(target__targetsname__icontains=query) |
            Q(mechanisms__mechanismname__icontains=query) |
            Q(articles__articlename__icontains=query) |
            Q(synonyms__synonymsmname__icontains=query)  # Добавляем поиск по синонимам
        ).distinct()
    else:
        model = Chronobiotic.objects.all()

    # Пагинация
    paginator = Paginator(model, 25)  # По 25 записей на страницу
    page_number = request.GET.get('page')  # Получаем текущую страницу из запроса
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы

    return render(request, 'main/index.html', {'page_obj': page_obj, 'query': query})

def about(request):
    return render(request, 'main/about.html')
def publications(request):
    return render(request, 'main/publications.html')
def rawdata(request):
    return render(request, 'main/rawdata.html')
def substance_detail(request, linkname):
    substance = get_object_or_404(Chronobiotic, linkname=linkname)
    return render(request, 'main/substance_detail.html', {'substance': substance})
def get_synonyms(request, linkname):
    try:
        chronobiotic = Chronobiotic.objects.get(linkname=linkname)
        synonyms = list(chronobiotic.synonyms.all().values_list('synonymsmname', flat=True))
        return JsonResponse({'synonyms': synonyms})
    except Chronobiotic.DoesNotExist:
        return JsonResponse({'synonyms': []})
def publicationsrec(request):
    # Берем все записи из новой таблицы
    records = PublicationRecord.objects.filter(item_type='article')
    return render(request, 'main/publications.html', {'records': records})


def rawdata(request):
    # Фильтруем записи по типу 'date'
    records = PublicationRecord.objects.filter(item_type='date')
    return render(request, 'main/rawdata.html', {'records': records})
@ratelimit(key='ip', rate='6/m', block=True)
@require_POST
def chat_ajax(request):
    message = request.POST.get('message', '').strip()
    if not message:
        return JsonResponse({'reply': 'Empty question.'})

    try:
        response = requests.post(
            get_agent_url(),
            json={'question': message},
            headers={
                'Content-Type': 'application/json',
                'X-API-KEY': settings.AI_AGENT_KEY,
            },
            timeout=150
        )
        if response.status_code == 200:
            data = response.json()
            answer = data.get('answer', 'No answer.')
            cards_used = data.get('cards_used', [])
            card_names = data.get('card_names', [])
            time_seconds = data.get('time_seconds', 0.0)

            # Сохраняем в БД
            ChatLog.objects.create(
                question=message,
                answer=answer,
                cards_used=cards_used,
                card_names=card_names,
                time_seconds=time_seconds,
            )

            # Проверяем — накопилось ли 100 записей
            if ChatLog.objects.count() >= 100:
                _dump_and_clean()

            return JsonResponse({'reply': answer})

        elif response.status_code == 403:
            return JsonResponse({'reply': 'Agent access error.'})
        elif response.status_code == 503:
            return JsonResponse({'reply': 'The agent is loading, please try again later.'})
        else:
            return JsonResponse({'reply': f'Error: {response.status_code}'})

    except requests.exceptions.Timeout:
        return JsonResponse({'reply': 'The agent thinks for a long time, try again.'})
    except requests.exceptions.ConnectionError:
        return JsonResponse({'reply': 'Failed to connect to agent.'})


def _dump_and_clean():
    logs = ChatLog.objects.order_by('created_at')

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['id', 'created_at', 'question', 'answer', 'cards_used', 'card_names', 'time_seconds'])
    for log in logs:
        writer.writerow([
            log.id,
            log.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            log.question,
            log.answer,
            ', '.join(map(str, log.cards_used)),
            ', '.join(log.card_names),
            log.time_seconds,
        ])

    email = EmailMessage(
        subject=f'ChronobioticsDB — chat dump ({logs.count()} records)',
        body='CSV with chat history attached.',
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.CHAT_LOG_RECIPIENT],
    )
    email.attach('chat_dump.csv', output.getvalue(), 'text/csv')
    email.send(fail_silently=True)

    last = ChatLog.objects.order_by('-created_at').first()
    ChatLog.objects.exclude(pk=last.pk).delete()