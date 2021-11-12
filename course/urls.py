from django.urls import path

from .views import courses  
#,coursesById ,updateListRegister

urlpatterns = [
    path('courses/',courses),
    # path('courses/<int:course_id>/',coursesById),
    # path('courses/<int:course_id>/registrations/',updateListRegister),
]


