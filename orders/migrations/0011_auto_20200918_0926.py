# Generated by Django 3.1.1 on 2020-09-18 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200918_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item',
            new_name='items',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart'),
        ),
    ]
