from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sign-up/', views.sign_up, name = 'sign_up'),
    path('<int:profile_id>/complete/', views.complete, name = 'complete'), 
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('check_id_duplicate/', views.check_id_duplicate, name = 'id_check'),
]

