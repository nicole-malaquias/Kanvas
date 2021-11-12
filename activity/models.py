from django.db import models
from django.db.models.deletion import CASCADE

class Activity(models.Model):
    
    title = models.CharField(max_length=254, unique=True)
    points = models.FloatField()
   
  

