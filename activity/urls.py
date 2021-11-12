from django.urls import path

from .views import  activity  

urlpatterns = [
    path('activities/',activity),
    path('activities/<int:activity_id>/',activity),
]


