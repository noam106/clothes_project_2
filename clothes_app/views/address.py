from ..models import IsraeliAddress
from ..serializers.address import IsraeliAddressSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from clothes_app.permissions_class.address import AddressPermission


class IsraeliAddressViewSet(viewsets.ModelViewSet):
    queryset = IsraeliAddress.objects.all()
    serializer_class = IsraeliAddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'district', 'postal_code']
    permission_classes = [AddressPermission]



