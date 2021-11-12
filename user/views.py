
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.serializer import UserSerializer

User = get_user_model()


@api_view(['POST'])
def login(request):
    
    user = authenticate(
          username=request.data['username'], 
          password=request.data['password']
        )

    if user:          
      
      token = Token.objects.get_or_create(user=user)
      str_token = token[0].key
      
      return Response({"token": str_token},status=status.HTTP_201_CREATED)  
      
    return Response(status=status.HTTP_401_UNAUTHORIZED) 


@api_view(['POST'])
def createUser(request):
    
    try:
      data = request.data
      user =''
      
      if data['is_staff'] == False and data['is_superuser'] == False :
        
        user = User.objects.create_user(
        username= data['username'], 
        password= data['password'],
        is_staff= False ,
        is_superuser = False)
      
      if data['is_staff'] == True and data['is_superuser'] == False :
        
        user = User.objects.create_user(
        username= data['username'], 
        password= data['password'],
        is_staff= True ,
        is_superuser = False)
  
      if data['is_staff'] == True and data['is_superuser'] == True :
       
        user = User.objects.create_superuser(
        username= data['username'], 
        password= data['password'],
        is_staff= True ,
        is_superuser = True)
     
      response = UserSerializer(user)
      return Response(response.data,status=status.HTTP_201_CREATED)
    
    except :
      
      return  Response(status=status.HTTP_409_CONFLICT)   
      
