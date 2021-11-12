from django.urls import path

from .views import login , createUser 

urlpatterns = [
    path('login/', login),
    path('accounts/',createUser),
]

