from rest_framework import permissions


class IsOwnerPermissions(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
