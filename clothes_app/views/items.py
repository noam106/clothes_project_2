import os
import uuid

import django_filters
from django.contrib.staticfiles import storage
from django_filters.rest_framework import FilterSet
from google.oauth2 import service_account
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, SAFE_METHODS, \
    IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from clothes_app.models import Item
from clothes_app.serializers.items import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response



class ItemPaginationClass(PageNumberPagination):
    page_size = 5


class ItemPermissions(BasePermission):
    # def has_permission(self, request, view):
    #     if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
    #         return request.user.is_staff
    #     return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve' or view.action == 'update':
            return request.user.is_staff or request.user == obj.user


class ItemFilterSet(FilterSet):
    min_price = django_filters.NumberFilter('price', lookup_expr='gte')
    max_price = django_filters.NumberFilter('price', lookup_expr='lte')
    price = django_filters.RangeFilter(field_name='price')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    item_type = django_filters.CharFilter(lookup_expr="icontains")
    colors = django_filters.CharFilter(lookup_expr='icontains')
    item_condition = django_filters.CharFilter(field_name='item_condition', lookup_expr='icontains')
    user = django_filters.NumberFilter()

    class Meta:
        model = Item
        fields = ['name', 'item_type', 'colors', 'item_condition', 'price']


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilterSet
    permission_classes = [IsAuthenticatedOrReadOnly, ItemPermissions, IsAuthenticated]
    pagination_class = ItemPaginationClass


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_item_img(request):
    bucket_name = 'suitapp'
    file_stream = request.FILES['file'].file
    _, ext = os.path.splitext(request.FILES['file'].name)

    object_name = f"profile_img_{uuid.uuid4()}{ext}"

    credentials = service_account.Credentials.from_service_account_file(
        'C:\\Users\\USER001\\Desktop\\Python_JB\\suitapp-service-account-key.json')

    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_file(file_stream)

    return Response()
