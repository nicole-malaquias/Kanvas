from django.db import models

class Course(models.Model):
    
    name = models.CharField(max_length=254, unique=True)
    users = models.ManyToManyField('user.User',related_name='courses')
  


