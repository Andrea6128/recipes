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
    context = { 'thisRecipe': currentRecipe,
                'thisIP': ip,
                'lastIP': lastIP,
                'thisForm': form }
    print(context)

    return render(request, 'recipe.html', context)

# success view
def success_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        # is_valid() needs to have required=True in every form item
        if form.is_valid():
            selected = form.cleaned_data.get("radio_button")
            print("selected=", selected)
            return render(request, 'success.html', {'selected': selected })
    else:
        return HttpResponse('An error occured!')
