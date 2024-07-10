from django.shortcuts import render
from .models import Pokemon

def index(request):
    pokemon_list = Pokemon.objects.all()
    context = {"pokemon_list": pokemon_list}
    return render(request, "index.html", context)
