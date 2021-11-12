from django.db import models
from django.db.models.deletion import CASCADE


class Submission(models.Model):
    
    grade = models.FloatField(null=True,blank=True, default=None)
    repo =  models.CharField(max_length=254)
    user = models.ForeignKey('user.User', on_delete=CASCADE)
    activity = models.ForeignKey('activity.Activity', on_delete=CASCADE, related_name='submissions')

