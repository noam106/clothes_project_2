from django.urls import path
from rest_framework.routers import DefaultRouter

from clothes_app.views.items import ItemsViewSet

# automatically defining urls for MoviesViewSet
router = DefaultRouter()
router.register('', itemsViewSet)

urlpatterns = []

# adding movies urls to urlpatterns
urlpatterns.extend(router.urls)