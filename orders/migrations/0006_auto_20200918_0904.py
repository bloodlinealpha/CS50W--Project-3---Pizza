# Generated by Django 3.1.1 on 2020-09-18 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_cart_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.pizza'),
        ),
    ]
