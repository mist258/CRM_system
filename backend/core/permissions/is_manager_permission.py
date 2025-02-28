from rest_framework.permissions import BasePermission


class IsManagerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and
                    not request.user.is_blocked and
                    request.user.is_staff)
