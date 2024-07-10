from django.contrib import admin
from pokemon.models import Pokemon, Type, Ability
# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(Ability)