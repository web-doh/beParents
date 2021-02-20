
from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [

    path('', views.index, name = 'index'),
    path('center_list/', views.center_list, name = 'center_list'),
    path('center_list_ajax/', views.center_list_ajax, name = 'center_list_ajax'),

]