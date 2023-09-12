from django.urls import include, path
from rest_framework import routers

from clothes_app.views.items import ItemViewSet,create_item

router = routers.DefaultRouter()
router.register(r'', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("item")
    #path('img/', upload_item_img),

]
