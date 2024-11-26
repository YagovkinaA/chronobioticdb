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
    model = Chronobiotic.objects.all()
    # context={
    #   model:model,
    # }
    return render(request,'main/index.html',{'model':model})
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