from django.db import models



class State(models.Model):
    name = models.CharField(max_length=100)
    

class City(models.Model):
    name = models.CharField(max_length=100)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
