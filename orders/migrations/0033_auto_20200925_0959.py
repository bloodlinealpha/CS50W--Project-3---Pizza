# Generated by Django 3.1.1 on 2020-09-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_auto_20200923_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], default='PENDING', max_length=32),
        ),
    ]
