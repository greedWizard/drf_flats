from django.db import models


class State(models.Model):
    name = models.CharField(max_length=350, unique=True)


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=350, unique=True)


