from django.db import models

# Create your models here.
class customers(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
