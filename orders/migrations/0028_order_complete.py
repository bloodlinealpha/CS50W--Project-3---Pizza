# Generated by Django 3.1.1 on 2020-09-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_cart_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]