# Generated by Django 3.1 on 2020-09-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20200907_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='servicefee',
        ),
        migrations.AddField(
            model_name='check',
            name='servicefree',
            field=models.IntegerField(default=20),
        ),
    ]
