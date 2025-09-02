#from django import forms
#from django.contrib.auth.models import AbstractUser
from django.db import models

#from multiselectfield import MultiSelectField

# Create your models here.
class Museum(models.Model):
    name = models.CharField()
    category = models.CharField() 
    city = models.TextField()     
    description = models.TextField()
    website = models.URLField()
    

    def __str__(self):
        return self.name
    
  
  
  
  
  
  
  
  
    
# class User(AbstractUser):
#     pass





# CATEGORIES = (('cat_1', 'Art'),
#               ('cat_2', 'Science'),
#               ('cat_3', 'History'),
#               ('cat_4', 'Natural History'),
#               ('cat_5', 'Cultural'),
#               ('cat_6', 'Children'),
#               ('cat_7', 'Interactive')
#               )

# class Category(forms.Form):
#     choices = forms.MultipleChoiceField = CATEGORIES