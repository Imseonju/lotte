from django.db import models
from user.models import CustomUser
# Create your models here.
class lent(models.Model):
    machine = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    inventory = models.IntegerField()
    provider = models.ManyToManyField(CustomUser) 