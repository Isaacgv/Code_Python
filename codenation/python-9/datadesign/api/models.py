from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

def validate_level(level):
    if level not in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']:
        raise ValidationError('Level not allowed')

class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])

class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(max_length=39, protocol='IPv4')

class Event(models.Model):
    level = models.CharField(max_length=20, validators=[validate_level])
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=50)

class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)