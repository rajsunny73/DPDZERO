from django.db import models

# Create your models here.

class RegisterModels(models.Model):
    userName = models.CharField(max_length=30)
    email= models.EmailField()
    password= models.CharField(max_length=30)
    fullName =models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    age=models.IntegerField()

class TokenModels(models.Model):
    userName = models.CharField(max_length=30)
    password= models.CharField(max_length=30)

class StorageModels(models.Model):
    key = models.CharField(max_length=30)
    value= models.CharField(max_length=30)    

