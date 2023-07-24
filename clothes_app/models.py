from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from address.address import *
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField


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
    CONDITION = {
        "condition": [
            ("as new", "As New"),
            ("used", "Used"),
            ("Needed repair", "needed_repair"),
            ("In box", "in_box"),
        ]
    }
    METHODS = {
        "method": [
            ("pyment_delivery", "Payment delivery"),
            ("pickup_from_seller", "Pickup from seller"),
            ("pickup_from_other_location", "Pickup from other location"),
            ("free_delivery", "Free delivery"),
            ("other", "Other"),
        ]
    }

    class Meta:
        db_table = "items"
        ordering = ['id']
    # name will be used as haeder for the item
    name = models.CharField(max_length=256, validators=[MinLengthValidator(4)], default='none', db_column='name',
                            null=False, blank=False)
    item_type = models.CharField(max_length=256, choices=CLOTHES_LIST['clothe'], db_column="item_type")
    colors = models.CharField(max_length=128, db_column='colors', null=False, blank=False,)
    description = models.TextField(db_column='description', null=True, blank=True)
    item_condition = models.CharField(max_length=256, choices=CONDITION['condition'], blank=True, null=True, db_column="item_condition")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_column="price", default=0)
    is_free = models.BooleanField(default=False, db_column='is free')
    delivery_method = models.CharField(max_length=256, choices=METHODS['method'], db_column="delivery_method", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.price == 0:
            self.is_free = True
        super().save(*args, **kwargs)


class IsraeliAddress(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=10,  null=True, blank=True)

    class Meta:
        db_table = "address"
        ordering = ['city', 'district', 'postal_code']

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.district}, {self.postal_code}'


class CustomerDetails(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.ForeignKey(IsraeliAddress, on_delete=models.PROTECT)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)


# class DeliveryMethods(models.Model):
#
#     class Meta:
#         db_table = "delivery_method"
#         ordering = ['id']
#
#     METHODS = {
#         "method": [
#             ("pyment_delivery", "Payment delivery"),
#             ("pickup_from_seller", "Pickup from seller"),
#             ("pickup_from_other_location", "Pickup from other location"),
#             ("free_delivery", "Free delivery"),
#             ("other", "Other"),
#         ]
#     }
#
#     method = models.CharField(max_length=128, choices=METHODS['method'], null=False, blank=False, db_column='method')
#
# # do i need to change the name to ItemDeliveryMethods???
#
#
# class ItemDeliveryMethods(models.Model):
#
#     class Meta:
#         db_table = "user_delivery_method"
#         ordering = ['id']
#
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     delivery_method = models.ForeignKey(DeliveryMethods, on_delete=models.CASCADE)
#     # address = AddressField(on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)


class ItemInterest(models.Model):

    class Meta:
        db_table = "items_interest"
        ordering = ['id']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Review(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_set')
    reviewed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewed_set')

    rating = models.SmallIntegerField(
        db_column='rating', null=False, validators=[MinValueValidator(1), MaxValueValidator(10)])
    review_text = models.TextField(
        db_column='review_text', null=True, blank=True
    )

    created_at = models.DateField(db_column='created_at', null=False, auto_now_add=True)

    class Meta:
        db_table = 'reviews'
