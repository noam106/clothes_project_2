import django_filters
from django_filters.rest_framework import FilterSet
from rest_framework import viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, SAFE_METHODS
from rest_framework.viewsets import GenericViewSet

from clothes_app.models import Item
from clothes_app.serializers.items import ItemSerializer


class ItemPaginationClass(PageNumberPagination):
    page_size = 15


class ItemPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_staff
        return True

