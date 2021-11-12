from rest_framework import serializers 
from user.serializer import UserSerializerClean
from user.models import User
from .models import Course  


class CourseSerializer(serializers.ModelSerializer):
 
    users = UserSerializerClean(many=True, read_only=True)
    
    class Meta:
        model=Course
        fields=['id','name','users']

        read_only_fields = ['id']
       