# Generated by Django 3.1.1 on 2020-09-21 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200918_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='items',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
    ]
