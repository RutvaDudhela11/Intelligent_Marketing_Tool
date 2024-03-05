# from datetime import timezone
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.CharField(null=True, max_length=25)
  joined_date = models.DateField(null=True)
  whatsapp = models.CharField(null=True, max_length=25)

class Country(models.Model):
    # id = models.AutoField( primary_key = True)
  name = models.CharField(max_length=100)
    
  def __str__(self):
    return self.name
    
class State(models.Model):
  # state_id = models.IntegerField, primary_key = True
  country =  models.ForeignKey(Country, on_delete=models.CASCADE)
  state_name = models.CharField(max_length=100)
  
  def __str__(self):
    return str(self.state_name)
        
class City(models.Model):
      # city_id= models.IntegerField, primary_key = True
  country =  models.ForeignKey(Country, on_delete=models.CASCADE) 
  state =  models.ForeignKey(State, on_delete=models.CASCADE) 
  city_name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.city_name

class Category(models.Model):
 # id =  models.Integer, primary_key = True, autoincrement=True
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class Url(models.Model):
  # uid =  models.Integer, primary_key = True, autoincrement=True
  country =   models.ForeignKey(Country, on_delete=models.CASCADE) 
  state =   models.ForeignKey(State, on_delete=models.CASCADE) 
  city =   models.ForeignKey(City, on_delete=models.CASCADE) 
  category =   models.ForeignKey(Category, on_delete=models.CASCADE) 
  url = models.URLField(max_length=1000, unique=True) 
    
  def __str__(self):
    return self.url

class Details(models.Model):
    # uid =  models.Integer, primary_key = True, autoincrement=True
  country =   models.ForeignKey(Country, on_delete=models.CASCADE) 
  state =   models.ForeignKey(State, on_delete=models.CASCADE) 
  city =   models.ForeignKey(City, on_delete=models.CASCADE) 
  category =   models.ForeignKey(Category, on_delete=models.CASCADE)
  url = models.URLField(max_length=1000) 
  name =  models.CharField(max_length=300)
  address = models.TextField(max_length=500, null=True)
  distance = models.TextField(max_length=200)
  time  = models.TextField(max_length=200)
  website = models.URLField(max_length=400, null=True) 
  phone_no = models.CharField(max_length=100, null=True) 
  created_at = models.DateTimeField(auto_now_add=True,null= True)
  updated_at = models.DateTimeField(auto_now=True, null=True)
  whatsapp = models.CharField(max_length=50, null=True)

  def __str__(self):
    return self.name 
  
class UploadImage(models.Model):
  Image = models.ImageField(upload_to='images/')