from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

# class CanCreatePropertyPermission(BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user is authenticated and is an agent
#         if request.user.is_active and request.user.is_agent:
#             return True
#         return False



class CanCreatePropertyPermission(BasePermission):
    message = {"You must complete your profile to create, view or accept tasks, click on this link: http://127.0.0.1:8000/users/profile/"}
    def CanCreatePropertyPermission(self, request, view):
        
        check = bool(request.user.is_agent)
        if check == False:
            raise PermissionDenied(detail=self.message)
        return bool(request.user.is_agent)