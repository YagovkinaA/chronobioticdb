from django.shortcuts import render, get_object_or_404
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
def substance_detail(request, linkname):
    substance = get_object_or_404(Chronobiotic, linkname=linkname)
    return render(request, 'main/substance_detail.html', {'substance': substance})