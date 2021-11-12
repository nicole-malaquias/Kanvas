
from rest_framework import serializers 
from .models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Submission
        fields=['id','grade','repo','user_id','activity_id']
       
