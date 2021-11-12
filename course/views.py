from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.response import Response

from user.permissions import InstructorPermission 
from .permissions import CoursesPermission ,CoursesByIdPermission

from course.serializer import CourseSerializer

from .models import Course
from django.contrib.auth import get_user_model 
User = get_user_model()

@api_view(['POST','GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([CoursesPermission])  
def courses(request):

    if request.method == 'POST' :
      
      course = Course.objects.get_or_create(name=request.data['name'])
      
      if course[1] == True :
        response = CourseSerializer(course[0])

        return Response(response.data,status=status.HTTP_201_CREATED)

      return Response({'error':'Course with this name already exists'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET' :
      
      course = Course.objects.all()
      serializer = [CourseSerializer(i) for i in course]
      response = [course.data for course in serializer]
      
      return Response(response)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([InstructorPermission])
def updateListRegister(request,course_id=""):
      
      try:
        data = request.data
        
        lista = data['user_ids']
        
        if type(lista) != list :
          
          return Response(status=status.HTTP_400_BAD_REQUEST)
        
        course = Course.objects.get(id=course_id)

        course.users.clear()

        for id in data['user_ids'] :
          
          student = User.objects.get(id=id)
          
          if student.is_superuser == True or student.is_staff == True :
            
            return Response({"errors": "Only students can be enrolled in the course."},status=status.HTTP_400_BAD_REQUEST)
          
          course.users.add(student)
          
          course.save()
          
        response = CourseSerializer(course)          
          
        return  Response(response.data, status=status.HTTP_200_OK)
        
      except:
        
        return Response({"errors": "invalid course_id"},status=status.HTTP_404_NOT_FOUND)
      

@api_view(['PUT','DELETE','GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([CoursesByIdPermission])
def coursesById( request, course_id=""):
  
  data = request.data
  
  if request.method == 'GET':
    
    try :
    
        if course_id == '' :
          course = Course.objects.all()
          serializer = [CourseSerializer(i) for i in course]
          response = [course.data for course in serializer]
          return Response(response)

        course = Course.objects.get(id=course_id)
        response = CourseSerializer(course)
        return Response(response.data,status=status.HTTP_200_OK)
      
    except:
        return Response({"errors": "invalid course_id"},status=status.HTTP_404_NOT_FOUND)
         
  if request.method == 'PUT':
     
      try:
        
        query = Course.objects.filter(name=data['name'])
        
        if len(query) > 0 :
          return Response( { 'error': 'Course with this name already exists'},status=status.HTTP_400_BAD_REQUEST)
        
        course = Course.objects.get(id=course_id)
        
        course.name = request.data['name']
        course.save()
        
        response = CourseSerializer(course)
        
        
        return  Response(response.data, status=status.HTTP_200_OK)
      
      except:
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
  if request.method == 'DELETE':
    
      try :
    
        Course.objects.get(id=course_id).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
      except :
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
   
