from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

class State(models.Model):
    name = models.CharField(max_length=100)
    

class City(models.Model):
    name = models.CharField(max_length=100)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, null=True)