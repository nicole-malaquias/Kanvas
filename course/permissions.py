from rest_framework.permissions import BasePermission

class CoursesPermission(BasePermission) :
    
    def has_permission(self, request, view) :
        
        if request.method == 'POST' and request.user.is_superuser == True :
            return True
           
        if request.method == 'GET' :
            
            return True 

class CoursesByIdPermission(BasePermission) :
    
    def has_permission(self, request, view) :
        
        methods =['DELETE', 'GET', 'PUT']
        
        if request.method in methods : 
            
           if request.user.is_superuser == True or request.user.is_staff ==  True :
               return True
        
        if request.method in methods :
            
            if request.user.is_superuser == True :
               return True
           
        if request.method in methods :
            return True 
        
