from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from clothes_app.models import Item, ItemInterest


# Create your views here.
@api_view(['GET'])
def stats(request):
    total_items = Item.objects.count()
    total_users = User.objects.count()
    total_item_intrest = ItemInterest.objects.count()

    ret_val = {
        'total_movies': total_items,
        'total_users': total_users,
        'total_reviews': total_item_intrest
    }
    return Response(ret_val)
