# Generated by Django 4.2.2 on 2023-08-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes_app', '0010_alter_customerdetails_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetails',
            name='img_url',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]