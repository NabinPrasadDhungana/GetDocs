from rest_framework.permissions import BasePermission

class AllowAnyForGet(BasePermission):

    def has_permission(self, request, view):
        print(view)
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE'] and not request.user.is_authenticated:
            return False
        return True
        