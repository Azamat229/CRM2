# Generated by Django 3.1 on 2020-09-09 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_check_mealtoorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='mealtoorder',
        ),
    ]
