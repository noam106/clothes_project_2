from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from clothes_app.views.auth import signup, me, upload_profile_img, google_login

urlpatterns = [
    path('signup/', signup),
    # given
    path('token/', TokenObtainPairView.as_view()),
    # given
    path('token/refresh/', TokenRefreshView.as_view()),
    path('google-auth', google_login),
    path('me/', me),
    path('me/img', upload_profile_img),


]