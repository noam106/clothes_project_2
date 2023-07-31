from rest_framework import serializers

from clothes_app.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['user']

    def create(self, validated_data):
        user_sent_request = self.context['request'].user
        validated_data['user'] = user_sent_request
        return super().create(validated_data)