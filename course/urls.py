from django.urls import path

from .views import courses  ,updateListRegister,coursesById

urlpatterns = [
    path('courses/',courses),
    path('courses/<int:course_id>/',coursesById),
    path('courses/<int:course_id>/registrations/',updateListRegister),
]


