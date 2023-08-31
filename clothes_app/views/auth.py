from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from clothes_app.serializers.auth import SignupSerializer, UserSerializer, UserCustomerSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
import os.path
import uuid
from rest_framework.response import Response
from google.oauth2 import service_account
from google.cloud import storage
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework_simplejwt.tokens import RefreshToken


# class UserViewSet(ModelViewSet):
#
#     serializer_class = UserSerializer
#     queryset = User.
class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address': user.profile.address
        }
        return JsonResponse(data)


@api_view(['POST'])
def signup(request):
    signup_serializer = SignupSerializer(data=request.data, many=False)
    if signup_serializer.is_valid(raise_exception=True):

        # only staff can create staff
        if signup_serializer.validated_data['is_staff']:
            if not (request.user.is_authenticated and request.user.is_staff):
                return Response(status=status.HTTP_401_UNAUTHORIZED,
                                data={'is_staff': ['Only staff member can create staff user']})

        new_user = signup_serializer.create(signup_serializer.validated_data)
        user_serializer = UserSerializer(instance=new_user, many=False)
        return Response(data=user_serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    # you will get here only if the user is already authenticated!
    user_serializer = UserCustomerSerializer(instance=request.user, many=False)
    return Response(data=user_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_img(request):
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

@api_view(['POST'])
def google_login(request):
    google_jwt = request.data['google_jwt']
    CLIENT_ID = '655087516681-m5jn8236hknlrh69cvqglh92tvb5hq09.apps.googleusercontent.com'
    try:
        idinfo = id_token.verify_oauth2_token(google_jwt, requests.Request(), CLIENT_ID)
        email = idinfo['email']
        try:
            user = User.objects.get(email=email)
            print('user found')
            print(user)
            # creating jwt manually

        except User.DoesNotExist:
            print('does not exist')
            user = User.objects.create_user(username=email, email=email, password=str(uuid.uuid4()),
                                     first_name=idinfo['given_name'], last_name=idinfo['family_name'])

        refresh = RefreshToken.for_user(user)
        return Response(data={
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

        print(idinfo)
    except ValueError as e:
        print(e)
    print(google_jwt)
    return Response()

