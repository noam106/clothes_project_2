from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.address import IsraeliAddressViewSet

router = DefaultRouter()
router.register(r'', IsraeliAddressViewSet)

# app_name = 'clothes_app'

urlpatterns = [
    path('', include(router.urls)),
]
