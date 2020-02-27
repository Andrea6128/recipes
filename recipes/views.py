from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Recipe
from datetime import datetime
import requests
from ipware import get_client_ip
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.

# homepage view with list of cities and links to them
def home_view(request):
    queryset = Recipe.objects.all()
    context = { 'recipes': queryset }
    return render(request, 'home_view.html', context)

# single recipe view by id
def recipe_id_view(request, id):
    currentRecipe = get_object_or_404(Recipe, id=id)
    ip_tuple = get_client_ip(request)

    ip = str(ip_tuple)
    removed_chars = ["'", "(", ")", ",", "False", " "]
    for char in removed_chars:
        ip = ip.replace(char, "")

    lastIP = ip

    form = UserForm()

    # if POST happened, store value
    # if request.method == 'POST':
    #     print('POST happened OK')
    #     # return render(request, 'printers/success.html', {'viewsRoomNumber': viewsRoomNumber, 'viewsPrinterName': viewsPrinterName, 'viewsTonerColor': viewsTonerColor })
    # else:
    #     print('POST didn\'t happen')
    context = { 'thisRecipe': currentRecipe,
                'thisIP': ip,
                'lastIP': lastIP,
                'thisForm': form }
                # 'thisWeatherType': weatherType,
                # 'thisWeatherDesc': weatherDesc,
                # 'thisWindSpeed': windSpeed,
                # 'thisCurrentTime': currentTime,
                # 'thisBgPic': bgPic }
    print(context)

    return render(request, 'recipe.html', context)

def success(request):
    form = UserForm(request.POST)

    if form.is_valid():
        selected = form.cleaned_data.get("RADIO_CHOICES")
        print(selected)

    return render(request, 'success.html', {'selected': selected})
