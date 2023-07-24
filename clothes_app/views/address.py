from rest_framework import generics
from ..models import IsraeliAddress
from ..serializers.address import IsraeliAddressSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class IsraeliAddressViewSet(viewsets.ModelViewSet):
    queryset = IsraeliAddress.objects.all()
    serializer_class = IsraeliAddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'district', 'postal_code']
    # filterset_class =
    # !!!DELETE AFTER CHEACING
    # permission_classes = [AllowAny]


# class IsraeliAddressList(generics.ListCreateAPIView):
#     queryset = IsraeliAddress.objects.all()
#     serializer_class = IsraeliAddressSerializer
#
#
# class IsraeliAddressDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = IsraeliAddress.objects.all()
#     serializer_class = IsraeliAddressSerializer
