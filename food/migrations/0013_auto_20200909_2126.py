# Generated by Django 3.1 on 2020-09-09 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_remove_check_mealtoorder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='check',
            old_name='order_id',
            new_name='orderid',
        ),
    ]
