from django.urls import path
from . import views

app_name = 'centers'

urlpatterns = [

    path('<int:center_id>/', views.index, name = 'index'),
    path('<int:center_id>/reviews/new', views.reviews, name = 'reviews'),
    path('<int:center_id>/reviews/save', views.save, name = 'save'),
    path('<int:center_id>/<int:review_id>/edit', views.edit, name = 'edit'),
    path('<int:center_id>/<int:review_id>/update', views.update, name = 'update'),
    path('<int:center_id>/<int:review_id>/delete/', views.delete, name = 'delete'),
    path('<int:center_id>/like/', views.like, name = 'like'),

]

