from rest_framework.permissions import BasePermission

class ActivityPermission(BasePermission):
    
    def has_permission(self, request, view):
        
        methods = ['GET','POST','PUT']
        
        if request.method in methods : 
          
           if request.user.is_superuser == True or request.user.is_staff ==  True :
               
               return True
           
  
        