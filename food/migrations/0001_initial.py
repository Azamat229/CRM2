# Generated by Django 3.1 on 2020-09-10 09:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(help_text='option field', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePercentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Userr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dateofadd', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('phone', models.IntegerField(help_text='996559444345')),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.role')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isitopen', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tableid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.table')),
                ('waiterid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.userr')),
            ],
        ),
        migrations.CreateModel(
            name='MealsToOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_meal', models.PositiveIntegerField()),
                ('mealsid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.meal')),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals_id', to='food.order')),
            ],
        ),
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('departmentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.department')),
            ],
        ),
        migrations.CreateModel(
            name='MealCategoriesByDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('departmentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.department')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.mealcategory'),
        ),
        migrations.CreateModel(
            name='GetUserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.role')),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('servicefree', models.IntegerField(default=20)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='food.order')),
            ],
        ),
    ]
