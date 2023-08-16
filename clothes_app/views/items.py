import django_filters
from django_filters.rest_framework import FilterSet
from rest_framework import viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, SAFE_METHODS, \
    IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from clothes_app.models import Item
from clothes_app.serializers.items import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend


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
    permission_classes = [IsAuthenticatedOrReadOnly, ItemPermissions]
    pagination_class = ItemPaginationClass
