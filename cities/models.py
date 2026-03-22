from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    population = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name