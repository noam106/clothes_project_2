from rest_framework.permissions import BasePermission


class ItemsPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve' or view.action == 'update':
            return request.user.is_stuff or request.user == obj.user
