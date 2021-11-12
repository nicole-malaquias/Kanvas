

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.response import Response
from .permissions import ActivityPermission
from activity.serializer import ActivitySerializer
from .models import Activity


@api_view(['POST','GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([ActivityPermission])
def activity(request,activity_id=""):  
    
    data = request.data
    
    if request.method == 'POST':
       
        activity = Activity.objects.filter(title=data['title']).exists()
        
        if not activity :
            
            activity = Activity.objects.create(**data)
       
            response = ActivitySerializer(activity)

            return Response(response.data,status=status.HTTP_201_CREATED)
        
        return Response( {'error': 'Activity with this name already exists'},status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        
        course = Activity.objects.all()
        serializer = [ActivitySerializer(i) for i in course]
        response = [course.data for course in serializer]
            
        return Response(response,status=status.HTTP_200_OK)


    if request.method == 'PUT':
        
        try:
           
            if activity_id != '' :
            
                activity = Activity.objects.get(id=activity_id)
                serializer = ActivitySerializer(activity)
                
                if len(serializer.data['submissions']) == 0:
                    
                    if 'title' in data :
                        
                      if data['title'] != activity.title :
                      
                        query = Activity.objects.filter(title=data['title'])
                        
                        if len(query) > 0 :
                            
                            return Response({ 'error': 'Activity with this name already exists'},status=status.HTTP_400_BAD_REQUEST)
                    
                    
                    
                    activity.title = data.get('title',activity.title)
                    
                    activity.points = data.get('points',activity.points)
                    
                    activity.save()
                    
                    response = ActivitySerializer(activity)
                    
                        
                    return Response(response.data,status=status.HTTP_200_OK)
                
                return Response({'error': 'You can not change an Activity with submissions'},status=status.HTTP_400_BAD_REQUEST)

            
        except :
            
            return Response(status=status.HTTP_404_NOT_FOUND)
        
  

