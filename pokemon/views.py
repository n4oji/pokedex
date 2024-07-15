from django.shortcuts import render  # type: ignore
from .models import Pokemon, Type, Ability
from django.http import HttpResponse  # type: ignore
import requests


def index(request):
    pokemon_list = Pokemon.objects.all()
    context = {"pokemon_list": pokemon_list}
    return render(request, "index.html", context)


def fecth_types(request):
    url = 'https://pokeapi.co/api/v2/type/'

    for i in range(19):
        request = requests.get(url+str(i+1))
        if request.status_code == 200:
            json = request.json()
            pkmn_type = Type.objects.get_or_create(name=json['name'])
            if pkmn_type[1] == True:
                print(f'Type {pkmn_type[0].name} created.')
            else:
                print(f'Type {pkmn_type[0].name} already exists.')
        else:
            print(request.status_code)

    return HttpResponse('Types imported from PokeAPI.')


def fecth_pokemon(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'

    for i in range(151):
        request = requests.get(url+str(i+1))
        if request.status_code == 200:
            json = request.json()
            pkmn, created = Pokemon.objects.get_or_create(number=json['id'],
                                                          name=json['name'],)
            if created:
                for type in json['types']:
                    pkmn.types.add(Type.objects.get(
                        name=type['type']['name']))

                for ability in json['abilities']:
                    pkmn_ability, created = Ability.objects.get_or_create(
                        name=ability['ability']['name'])
                    pkmn.abilities.add(pkmn_ability)

                pkmn.image = json['sprites']['front_default']
                pkmn.height = json['height']
                pkmn.weight = json['weight']
                pkmn.hp = json['stats'][0]['base_stat']
                pkmn.attack = json['stats'][1]['base_stat']
                pkmn.defense = json['stats'][2]['base_stat']
                pkmn.special_attack = json['stats'][3]['base_stat']
                pkmn.special_defense = json['stats'][4]['base_stat']
                pkmn.speed = json['stats'][5]['base_stat']

                pkmn.save()

                print(f'Pokemon {pkmn.name} created.')
            else:
                print(f'Pokemon {pkmn.name} already exists.')
        else:
            print(request.status_code)

    return HttpResponse('Pokemons imported from PokeAPI.')
