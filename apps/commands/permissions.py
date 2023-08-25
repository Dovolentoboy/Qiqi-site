from django.contrib.auth.models import PermissionManager

class CanDeleteCommand(PermissionManager):
    def delete_command(self, request, view):
        return request.user and request.user.is_staff
    
    def update_command(self, request, view):
        return request.user and request.user.is_staff
    
