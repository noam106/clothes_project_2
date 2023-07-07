from django.db import models
from django.contrib.auth.models import User
# from address.address import *
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class Item(models.Model):

    CLOTHES_LIST = {
        'clothe': [
            ('sweater', 'Sweater'),
            ('jacket', 'Jacket'),
            ('pants', 'Pants'),
            ('vest', 'Vest'),
            ('coat', 'Coat'),
            ('dress', 'Dress'),
            ('jeans', 'Jeans'),
            ('shirt', 'Shirt'),
            ('shorts', 'Shorts'),
            ('swimsuit', 'Swimsuit'),
            ('skirt', 'Skirt'),
            ('sock', 'Sock'),
            ('pajamas', 'Pajamas'),
            ('cardigan', 'Cardigan'),
            ('suit', 'Suit'),
            ('raincoat', 'Raincoat'),
            ('sleeveless_shirt', 'Sleeveless shirt'),
            ('belt', 'Belt'),
            ('other', 'Other'),

        ]
    }

    class Meta:
        db_table = "items"
        ordering = ['id']
    # name will be used as haeder for the item
    name = models.CharField(max_length=256, validators=[MinLengthValidator(4)], default='none', db_column='name',
                            null=False, blank=False)
    item_type = models.CharField(max_length=256, choices=CLOTHES_LIST['clothe'], db_column="item type")
    colors = models.CharField(max_length=128, db_column='colors', null=False, blank=False,)
    description = models.TextField(db_column='description', null=True, blank=True)
    item_condition = models.ForeignKey('ItemCondition', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_column="price", default=0)
    is_free = models.BooleanField(default=False, db_column='is free')

    def save(self, *args, **kwargs):
        if self.price == 0:
            self.is_free = True
        super().save(*args, **kwargs)


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

# do i need to change the name to ItemDeliveryMethods???


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
