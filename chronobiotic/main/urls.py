
from django.urls import path
from . import views
urlpatterns = [

    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('substance/<slug:linkname>/', views.substance_detail, name='substance_detail'),
    # path('index/<int:chronobiotic_id>',views.chronobiotic),
]
