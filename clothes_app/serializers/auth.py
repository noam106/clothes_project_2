from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from clothes_app.models import CustomerDetails
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import os.path
import uuid
from rest_framework.response import Response
from google.oauth2 import service_account
from google.cloud import storage


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'is_staff', "phone_number")

    email = serializers.EmailField(
        write_only=True,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, allow_null=False, allow_blank=False)
    first_name = serializers.CharField(write_only=True, required=True, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(write_only=True, required=True, allow_blank=False, allow_null=False)
    phone_number = serializers.CharField(write_only=True, required=True, allow_blank=False, allow_null=False,
                                         max_length=10)

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                is_staff=validated_data['is_staff'],
            )
        user.set_password(validated_data['password'])
        user.save()
        customer_details = CustomerDetails.objects.create(user=user, phone_number=validated_data['phone_number'])

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_staff')


class UserCustomerSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        user_repr = super().to_representation(instance)
        try:
            user_repr['img_url'] = instance.customer_dateils.img_url
            user_repr['address'] = instance.customer_dateils.address.street_address, instance.customer_dateils.address.city,\
                instance.customer_dateils.address.district, instance.customer_dateils.address.postal_code

            # user_repr['address'] = instance.customer_dateils.street_address.street_address
            # user_repr['address'] = instance.customer_dateils.postal_code.postal_code
            # user_repr['address'] = instance.customer_dateils.district.district
            user_repr['phone_number'] = instance.customer_dateils.phone_number
        except:
            user_repr['img_url'] = None
            user_repr['address'] = None
            user_repr['phone_number'] = None
        print(user_repr)
        return user_repr

    class Meta:
        model = User
        fields = ("id", 'email', 'first_name', 'last_name', 'is_staff')
