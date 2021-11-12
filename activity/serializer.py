from .models import Activity
from rest_framework import serializers 
from submission.serializer import SubmissionSerializer
class ActivitySerializer(serializers.ModelSerializer):

    submissions = SubmissionSerializer(many=True, read_only=True)
    
    class Meta:
        model=Activity
        fields=['id','title','points','submissions']
       
 
