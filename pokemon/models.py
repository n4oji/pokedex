from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name    
    
class Ability(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    types = models.ManyToManyField('Type', related_name="pokemon_types")
    abilities = models.ManyToManyField('Ability', related_name="pokemon_abilities")
    evolutions = models.ManyToManyField('self', symmetrical=False, related_name='pre_evolutions', blank=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    hp = models.PositiveIntegerField(blank=True, null=True)
    attack = models.PositiveIntegerField(blank=True, null=True)
    defense = models.PositiveIntegerField(blank=True, null=True)
    special_attack = models.PositiveIntegerField(blank=True, null=True)
    special_defense = models.PositiveIntegerField(blank=True, null=True)
    speed = models.PositiveIntegerField(blank=True, null=True)
    #types TODO
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.number} - {self.name}"
    
