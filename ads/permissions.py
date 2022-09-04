from rest_framework import permissions
from authentication.models import User


class AdUpdatePermission(permissions.BasePermission):
    message = 'Ads can be updated by ad owner, moderator or admin only.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.MEMBER and obj.author != request.user:
            return False
        return True


class AdDeletePermission(permissions.BasePermission):
    message = 'Ads can be deleted by ad owner, moderator or admin only.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.MEMBER and obj.author != request.user:
            return False
        return True


class SelectionUpdatePermission(permissions.BasePermission):
    message = 'Selections can only be updated by selection owners'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class SelectionDeletePermission(permissions.BasePermission):
    message = "Selections can only be deleted by selection owners."

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
