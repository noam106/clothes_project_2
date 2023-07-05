from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from clothes_app.views.reviews import ReviewsViewSet

router = DefaultRouter()
router.register('', ReviewsViewSet)

urlpatterns = []

# adding reviews urls to urlpatterns
urlpatterns.extend(router.urls)