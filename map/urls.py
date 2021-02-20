
from django.urls import path

from . import views

app_name = 'map'

urlpatterns = [
    path('', views.index, name = 'index'),
    #path('<int:center_id>/center_summary/', views.center_summary, name = 'center_summary'),
    path('ajax/', views.ajax, name = 'ajax'),
]