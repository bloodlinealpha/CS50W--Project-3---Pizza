# Generated by Django 3.1.1 on 2020-09-22 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20200922_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart'),
        ),
    ]