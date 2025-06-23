from rest_framework.permissions import BasePermission


class IsOrderOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.manager is None or obj.manager == request.user)
