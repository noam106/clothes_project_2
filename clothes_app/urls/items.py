from django.urls import include, path
from rest_framework import routers

from clothes_app.views.items import ItemViewSet

router = routers.DefaultRouter()
router.register(r'', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
