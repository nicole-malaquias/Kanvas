from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.permissions import StudentPermission
from activity.permissions import ActivityPermission
from submission.serializer import SubmissionSerializer
from .models import Submission

from activity.models import Activity
from django.contrib.auth import get_user_model 
User = get_user_model()

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([StudentPermission])
def submission(request,activity_id=""):  
    
    user = request.user
    data = request.data
    
    if activity_id != '' :
       
        activity = Activity.objects.get(id=activity_id)
    
        user = User.objects.get(username=user)
        
        repo = data.get('repo')
       
        submission = Submission.objects.create(repo=repo,user=user,activity=activity)

        
        activity.submissions.add(submission)
        activity.save()
        response = SubmissionSerializer(submission)
        
    return Response(response.data,status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication]) 
@permission_classes([ActivityPermission])
def updateGrade(request,submission_id=''):
  
    data = request.data

    if submission_id != '' :
        
        submission = Submission.objects.get(id=submission_id)
        
        grade = data.get('grade',None)

        submission.grade = grade
        submission.save()
        
        response = SubmissionSerializer(submission)
        
    return Response(response.data,status=status.HTTP_200_OK)
    
    # except:
        
    #     return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@authentication_classes([TokenAuthentication]) 
@permission_classes([IsAuthenticated])
def mySubmission(request):
    
  
    user = request.user
    user_id = user.id
  
    try:
        
        if user.is_staff == False and user.is_superuser == False :
        
            submission = Submission.objects.filter(user_id=user_id)
            serializer = [SubmissionSerializer(sub) for sub in submission]
            response = [course.data for course in serializer]
                
            return Response(response,status=status.HTTP_200_OK)
        
        submission = Submission.objects.all()
        serializer = [SubmissionSerializer(sub) for sub in submission]
        response = [course.data for course in serializer]  
           
        return Response(response,status=status.HTTP_200_OK)
    
    except:
        
        return Response(status=status.HTTP_404_NOT_FOUND)

