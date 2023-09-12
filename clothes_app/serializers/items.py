from rest_framework import serializers

from clothes_app.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

    # def create(self, validated_data):
    #     user_sent_request = self.context['request'].user
    #     validated_data['user'] = user_sent_request
    #     return super().create(validated_data)
