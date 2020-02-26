from django.urls import path
from . import views

# name='recipe_detail_view' means identifier from models.py reverse name
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('recipe/<int:id>/', views.recipe_id_view, name='recipe_detail_view'),
]
