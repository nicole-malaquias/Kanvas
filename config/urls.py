from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api/', include('course.urls')),
    # path('api/', include('activity.urls')),
    # path('api/', include('submission.urls')),
]
