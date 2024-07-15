from django.urls import path  # type: ignore
from .views import index, fecth_types, fecth_pokemon

urlpatterns = [
    path('', index, name='index'),
    path('fetch-types/', fecth_types, name='fetch-types'),
    path('fetch-pkmn/', fecth_pokemon, name='fetch-pkmn'),
]
