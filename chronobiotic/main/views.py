from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Chronobiotic

def index(request):
    query = request.GET.get('search', '')  # Получаем поисковый запрос
    if query:
        model = Chronobiotic.objects.filter(
            gname__icontains=query
        ) | Chronobiotic.objects.filter(
            molecula__icontains=query
        ) | Chronobiotic.objects.filter(
            fdastatus__icontains=query
        )
    else:
        model = Chronobiotic.objects.all()

    # Пагинация
    paginator = Paginator(model, 25)  # По 25 записей на страницу
    page_number = request.GET.get('page')  # Получаем текущую страницу из запроса
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы

    return render(request, 'main/index.html', {'page_obj': page_obj, 'query': query})

def about(request):
    return render(request, 'main/about.html')
