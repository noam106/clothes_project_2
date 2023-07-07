# Generated by Django 4.2.2 on 2023-07-07 06:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_free',
            field=models.BooleanField(db_column='is free', default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(db_column='name', default='none', max_length=256, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(blank=True, db_column='price', decimal_places=2, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('sweater', 'Sweater'), ('jacket', 'Jacket'), ('pants', 'Pants'), ('vest', 'Vest'), ('coat', 'Coat'), ('dress', 'Dress'), ('jeans', 'Jeans'), ('shirt', 'Shirt'), ('shorts', 'Shorts'), ('swimsuit', 'Swimsuit'), ('skirt', 'Skirt'), ('sock', 'Sock'), ('pajamas', 'Pajamas'), ('cardigan', 'Cardigan'), ('suit', 'Suit'), ('raincoat', 'Raincoat'), ('sleeveless_shirt', 'Sleeveless shirt'), ('belt', 'Belt'), ('other', 'Other')], db_column='item type', max_length=256),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(db_column='rating', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('review_text', models.TextField(blank=True, db_column='review_text', null=True)),
                ('created_at', models.DateField(auto_now_add=True, db_column='created_at')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes_app.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]
