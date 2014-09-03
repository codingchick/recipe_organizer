from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.ManyToManyField('Ingredient')
    description = models.TextField()
    instructions = models.TextField()

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name




