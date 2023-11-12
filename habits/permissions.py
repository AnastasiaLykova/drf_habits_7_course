from rest_framework.permissions import BasePermission


class IsCreator(BasePermission):
    message = 'вы не являетесь создателем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.creator:
            return True
        return False
