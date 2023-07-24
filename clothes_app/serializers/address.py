from rest_framework import serializers
from ..models import IsraeliAddress


class IsraeliAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsraeliAddress
        fields = ['id', 'street_address', 'city', 'district', 'postal_code']