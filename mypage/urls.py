
from django.urls import path

from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('mylikes/', views.mylikes, name = 'mylikes'),
    path('myreviews/', views.myreviews, name = 'myreviews'),
    path('myinfo/', views.myinfo, name = 'myinfo'),

   
]
