from django.urls import path

from .views import  submission  ,updateGrade,mySubmission

urlpatterns = [
    path('activities/<int:activity_id>/submissions/',submission),
    path('submissions/<int:submission_id>/',updateGrade),
    path('submissions/',mySubmission)

]


