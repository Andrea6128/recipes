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

    form = UserForm()
    context = { 'thisRecipe': currentRecipe,
                'thisForm': form,
                'id': id }
    print(context)
    print(id)
    print(currentRecipe.mealName)

    # store id number to temporary file
    with open("recipes/data/temp.json", "w") as out:
        data = str(id)
        out.write(data)

    return render(request, 'recipe.html', context)

# success view
def success_view(request):
    # get id from the file stored in recipe_id_view
    with open("recipes/data/temp.json", "r") as file:
        data_list = [id for id in next(file)]
        id = data_list[0]

    ip_tuple = get_client_ip(request)

    ip = str(ip_tuple)
    removed_chars = ["'", "(", ")", ",", "False", " "]
    for char in removed_chars:
        ip = ip.replace(char, "")

    lastIP = ip

    # check of POST request happened and process it
    if request.method == "POST":
        form = UserForm(request.POST)

        # is_valid() needs to have required=True in every form item
        if form.is_valid():
            selected = form.cleaned_data.get("radio_button")

            selectedInt = int(selected)

            # write current meal ID and IP address to the database
            Recipe.objects.filter(id=id).update(mealDbRating=selectedInt) # rating
            Recipe.objects.filter(id=id).update(mealIP=lastIP) # last visitor ip

            # todo: 2. calculate average rating for every meal and display it on the success page

            return render(request, 'success.html', {'selected': selected,
                                                    'lastIP': lastIP,
                                                   })
    else:
        return HttpResponse('An error occured!')
