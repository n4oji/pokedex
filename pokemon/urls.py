from django.urls import path  # type: ignore
from .views import index, fecth_types, fecth_pokemon, list_pkmns

urlpatterns = [
    path('', index, name='index'),
    path('list/', list_pkmns, name='list-pkmns'),
    path('fetch-types/', fecth_types, name='fetch-types'),
    path('fetch-pkmn/', fecth_pokemon, name='fetch-pkmn'),
]
