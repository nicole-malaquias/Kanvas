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
