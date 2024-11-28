# from django.http import HttpResponse
from django.shortcuts import render
from .models import Chronobiotic
from django.views import generic

# class ChronoListView(generic.ListView):
#     model = Chronobiotic
#     context_object_name ='chem_list'
#     def get_queryset(self):
#         return Chronobiotic.objects.all()

def index(request):
    query = request.GET.get('search', '')  # Получаем поисковый запрос из параметра search
    if query:
        # Фильтруем по имени, формуле или статусу
        model = Chronobiotic.objects.filter(
            gname__icontains=query
        ) | Chronobiotic.objects.filter(
            molecula__icontains=query
        ) | Chronobiotic.objects.filter(
            fdastatus__icontains=query
        )
    else:
        # Если нет поискового запроса, показываем всё
        model = Chronobiotic.objects.all()

    return render(request, 'main/index.html', {'model': model, 'query': query})
def about(request):
    return render(request,'main/about.html')
# def chrono(request):
#     model = Chronobiotic.objects.all()
#     # context={
#     #   model:model,
#     # }
#     return render(request,'main/index.html',{'model':model})
# def index(request)->HttpResponse:
#     return render(request,'main/index.html')
# def about(request)->HttpResponse:
#     return render(request,'main/about.html')
# def index(request):

#     context = {
#         'title': 'Home - Главная',
#         'content': "HOME",
#     }

#     return render(request, 'main/index.html', context)