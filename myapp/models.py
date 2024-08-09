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

#creating BloodRequest Model
class BloodRequest(models.Model):
  bloodchoices = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
  )
  title = models.CharField(max_length=100)
  blood_group = models.CharField(max_length=15, choices= bloodchoices)
  patient_name = models.CharField(max_length=100)
  hospital_name =  models.CharField(max_length=100)
  contact_number = models.CharField(max_length=10)
  requirement_date = models.DateField(null=True, blank=True)
  requirement_reason = models.CharField(max_length=150)
  is_expired = models.BooleanField(default=False)
  is_verified = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # def __str__(self):
  #   return self.name
