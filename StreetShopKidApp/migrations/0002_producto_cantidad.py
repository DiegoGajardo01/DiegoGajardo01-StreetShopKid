# Generated by Django 3.2.4 on 2022-11-09 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StreetShopKidApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]
