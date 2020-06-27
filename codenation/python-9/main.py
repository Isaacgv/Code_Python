from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)
    pasword = modles.CharField(max_lenght=50, validators= [MinLengthValidator(5)])

class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(max_length=39)

class Event(models.Model):
    level = models.CharField(max_length=20)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now=True)
    agent_id = models.ForeingKey(Agent, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=50)

class GroupUser(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)