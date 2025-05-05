from django.contrib.auth import get_user_model

from rest_framework.permissions import BasePermission

#UseModel = get_user_model()

class IsOrderOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.manager == request.user)