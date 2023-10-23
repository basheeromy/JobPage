"""
    Define custom permissions.
"""

from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser


class IsOwnerOrReadOnly(BasePermission):
    """
    Allows access only to owner of the database object
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
