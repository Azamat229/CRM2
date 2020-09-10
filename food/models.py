from django.db import models
import datetime
from django.contrib.auth.models import User


class Table(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Userr(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE)
    dateofadd = models.DateField(("Date"), default=datetime.date.today)
    phone = models.IntegerField(help_text="996559444345")

    def __str__(self):
        return self.name


class GetUserToken(models.Model):
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE)
    token = models.CharField(max_length=50)


class MealCategory(models.Model):
    name = models.CharField(max_length=50)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MealCategoriesByDepartment(models.Model):
    name = models.CharField(max_length=50)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    percentage = models.IntegerField(default=33)

    def __str__(self):
        return str(self.percentage)


class Meal(models.Model):
    name = models.CharField(max_length=50)
    category_id = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(help_text="option field", null=True, max_length=500)

    def __str__(self):
        return self.name


<<<<<<< HEAD
#
# class MealMealsByCategory(models.Model):
#     name = models.CharField(max_length=50)
#     categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     description = models.CharField(help_text="option field", null=True)
#
#     def __str__(self):
#         return self.name


=======
>>>>>>> 143fa8e4e217f0d7d478b33f1fcc8b4d00316a0d
class Order(models.Model):
    waiterid = models.ForeignKey(Userr, on_delete=models.CASCADE)
    tableid = models.ForeignKey(Table, on_delete=models.CASCADE)
    isitopen = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def table_name(self):
        return self.tableid.name

    def get_total(self):
        return sum(item.get_cost() for item in self.meals_id.all())

    def __str__(self):
        return '{}, {}'.format(self.waiterid, self.tableid)


<<<<<<< HEAD
class MealsToOrder(models.Model):
    orderid = models.ForeignKey(Order, related_name='meals_id', on_delete=models.CASCADE)
    count_meal = models.PositiveIntegerField()
    mealsid = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def get_cost(self): return self.mealsid.price * self.count_meal

    @property
    def total(self):
        return self.count_meal * self.mealsid.price


class Check(models.Model):
    orderid = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    servicefree = models.IntegerField(default=20)

    def __str__(self):
        return 'Check id {}, {}'.format(self.id, self.orderid)
=======
class CountOfMeal(models.Model):
    order = models.ForeignKey(Order, related_name='count', on_delete=models.CASCADE)
    name_meal = models.ForeignKey(Meal, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.PositiveIntegerField()

    @property
    def total(self):
        return self.amount * self.name_meal.price

    def __str__(self):
        return self.total


"""Create Check"""


class Check(models.Model):
    orderid = models.ForeignKey(Order, related_name='counts', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    servicefree = models.IntegerField(default=20)
    totalsum = models.IntegerField(blank=True, null=True)  # thinking about this
    mealsid = models.ForeignKey(CountOfMeal, on_delete=models.CASCADE)

    def __str__(self):
        return self.orderid
>>>>>>> 143fa8e4e217f0d7d478b33f1fcc8b4d00316a0d
