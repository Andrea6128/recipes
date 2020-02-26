from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Recipe
from datetime import datetime
import requests

# Create your views here.

# homepage view with list of cities and links to them
def home_view(request):
    queryset = Recipe.objects.all()
    context = { 'recipes': queryset }
    return render(request, 'home_view.html', context)

# single city view by id
def recipe_id_view(request, id):
    currentRecipe = get_object_or_404(Recipe, id=id)

    context = { 'thisRecipe': currentRecipe }
                # 'thisWeatherType': weatherType,
                # 'thisWeatherDesc': weatherDesc,
                # 'thisWindSpeed': windSpeed,
                # 'thisCurrentTime': currentTime,
                # 'thisBgPic': bgPic }
    return render(request, 'recipe.html', context)
