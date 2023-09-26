from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from clothes_app.models import Item, ItemInterest

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def items_of_intrest(request):
    intrested_items = ItemInterest.object.filter(request.user.id)