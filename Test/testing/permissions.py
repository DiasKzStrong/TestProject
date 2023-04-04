from rest_framework import permissions


class AllowPostandIsAdminpermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method == 'POST':
            return True
        
        return request.user.is_superuser
    
class OnlyAdminCanDelete(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return request.user.is_superuser
        return True
    
class NotFoundBlock(permissions.BasePermission):

    def has_permission(self, request, view):
        return False
    
    
class OnlyAdminPost(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_superuser
    
class EveryOneCanPUT(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'PUT':
            return True