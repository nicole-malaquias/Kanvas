from rest_framework import serializers 
from django.db.models.deletion import CASCADE

from django.contrib.auth import get_user_model 
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
  
    class Meta:
        model=User
        fields= ['id','username','is_superuser','is_staff']
        read_only_fields = ['id']
        

class UserSerializerClean(serializers.ModelSerializer):
    
  
    class Meta:
        model=User
        fields= ['id','username']
        read_only_fields = ['id']
        
