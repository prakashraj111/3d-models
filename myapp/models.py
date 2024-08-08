from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  age = models.IntegerField()

  def __str__(self):
    return self.name

#create customer model
class Customer(models.Model):
  name = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=255)
  address =  models.CharField(max_length=255)
  email = models.CharField(max_length=15)
  secondary_phone = models.CharField(max_length=15, null=True)