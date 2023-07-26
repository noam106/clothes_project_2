from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from clothes_app.views.auth import signup, me


urlpatterns = [
    path('signup/', signup),
    # given
    path('token/', TokenObtainPairView.as_view()),
    # given
    path('token/refresh/', TokenRefreshView.as_view()),
    path('me/', me),

]