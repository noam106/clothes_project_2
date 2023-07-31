from rest_framework import serializers
from ..models import IsraeliAddress


class IsraeliAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsraeliAddress
        fields = ['id', 'street_address', 'city', 'district', 'postal_code']

        def create(self, validated_data):
            user_sent_request = self.context['request'].user
            validated_data['user'] = user_sent_request
            return super().create(validated_data)