from rest_framework.permissions import BasePermission

class InstructorPermission(BasePermission):
    
    def has_permission(self, request, view):
        
       return request.user.is_superuser == True



class FacilitadorPermission(BasePermission):
    
    def has_permission(self, request, view):

       return request.user.is_superuser == False and request.user.is_staff ==  True 



class StudentPermission(BasePermission):
    
    def has_permission(self, request, view):

       return request.user.is_superuser == False and request.user.is_staff ==  False 
  