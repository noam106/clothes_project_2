from django.db import models
from django.contrib.auth.models import User
# from address.address import *
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Item(models.Model):

    CLOTHES_LIST = {
        'clothe': [
            ('Sweater', 'sweater'),
            ('Jacket', "jacket"),
            ("Pants", "pants"),
            ("Vest", "vest"),
            ("Coat", "coat"),
            ("Dress", "dress"),
            ("Jeans", "jeans"),
            ("Shirt", "shirt"),
            ("Shorts", "shorts"),
            ("Swimsuit", "swimsuit"),
            ("Skirt", "skirt"),
            ("Sock", "sock"),
            ("Pajamas", "pajamas"),
            ("Cardigan", 'cardigan'),
            ("suit", "Suit"),
            ("Raincoat", "raincoat"),
            ("sleeveless_shirt", "Sleeveless shirt"),
            ("Belt", "belt"),
            ("other", "Other"),
        ]
    }

    class Meta:
        db_table = "items"
        ordering = ['id']

    item_type = models.CharField(max_length=256, choices=CLOTHES_LIST['clothe'], db_column="item type")
    colors = models.CharField(max_length=128, db_column='colors', null=False, blank=False,)
    description = models.TextField(db_column='description', null=True, blank=True)
    item_condition = models.ForeignKey('ItemCondition', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ItemCondition(models.Model):

    class Meta:
        db_table = "item_condition"
        ordering = ['id']

    # CONDITION = {
    #     "condition": [
    #         ("as new", "As New"),
    #         ("used", "Used"),
    #         ("Needed repair", "needed_repair"),
    #         ("In box", "in_box"),
    #     ]
    # }

    condition = models.CharField(max_length=128, db_column="condition")
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)


class DeliveryMethods(models.Model):

    class Meta:
        db_table = "delivery_method"
        ordering = ['id']

    METHODS = {
        "method": [
            ("pyment_delivery", "Payment delivery"),
            ("pickup_from_seller", "Pickup from seller"),
            ("pickup_from_other_location", "Pickup from other location"),
            ("free_delivery", "Free delivery"),
            ("other", "Other"),
        ]
    }

    method = models.CharField(max_length=128, choices=METHODS['method'], null=False, blank=False, db_column='method')


class UserDeliveryMethods(models.Model):

    class Meta:
        db_table = "user_delivery_method"
        ordering = ['id']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_method = models.ForeignKey(DeliveryMethods, on_delete=models.CASCADE)
    # address = AddressField(on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class ItemInterest(models.Model):

    class Meta:
        db_table = "items_interest"
        ordering = ['id']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Review(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.SmallIntegerField(
        db_column='rating', null=False, validators=[MinValueValidator(1), MaxValueValidator(10)])
    review_text = models.TextField(
        db_column='review_text', null=True, blank=True
    )

    created_at = models.DateField(db_column='created_at', null=False, auto_now_add=True)

    class Meta:
        db_table = 'reviews'
