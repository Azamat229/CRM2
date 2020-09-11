from .models import *
from rest_framework import serializers

""" USER """


class UserListSerializer(serializers.ModelSerializer):
    roleid = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


"""MEAL"""


class MealListSerializer(serializers.ModelSerializer):
    categoryid = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Meal
        fields = '__all__'


class MealDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


"""Table"""


class TableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class TableDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


"""Role"""


class RoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RoleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


"""Department"""


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


"""MealCategory"""


class MealCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = '__all__'


class MealCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = '__all__'


"""MealCategory"""


class MealCategoriesByDepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategoriesByDepartment
        fields = '__all__'


"""MealCategory"""


class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class StatusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


"""MealCategory"""


class ServicePercentageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = '__all__'


class ServicePercentageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = '__all__'


"""Create and List Order"""


class MealsToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsToOrder
        fields = ['id', 'count_meal', 'mealsid', 'total']


class OrderSerializer(serializers.ModelSerializer):
    meals_id = MealsToOrderSerializer(many=True)
    total_sum = serializers.FloatField(source='get_total', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'waiterid', 'tableid', 'table_name', 'isitopen', 'total_sum', 'meals_id']

    def create(self, validated_data):
        meals_data = validated_data.pop('meals_id')
        orderid = Order.objects.create(**validated_data)
        for meal_data in meals_data:
            MealsToOrder.objects.create(**meal_data, orderid=orderid)
        return orderid


"""Update Order and meals"""


class OrderDetailSerializer(serializers.ModelSerializer):
    meals_id = MealsToOrderSerializer(many=True)
    total_sum = serializers.FloatField(source='get_total', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'waiterid', 'tableid', 'table_name', 'isitopen', 'total_sum', 'meals_id']

    def update(self, instance, validated_data):
        meals_data = validated_data.pop('meals_id')
        meals = (instance.meals_id).all()
        meals = list(meals)
        instance.waiterid = validated_data.get('waiterid', instance.waiterid)
        instance.tableid = validated_data.get('tableid', instance.tableid)
        instance.isitopen = validated_data.get('isitopen', instance.isitopen)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        for meal_data in meals_data:
            meal = meals.pop(0)
            meal.orderid = meal_data.get('orderid', meal.orderid)
            meal.count_meal = meal_data.get('count_meal', meal.count_meal)
            meal.mealsid = meal_data.get('mealsid', meal.mealsid)
            meal.save()
        return instance


"""List Check"""


class OrderSerializer2(serializers.ModelSerializer):
    meals_id = MealsToOrderSerializer(many=True)
    total_sum = serializers.FloatField(source='get_total', read_only=True)

    class Meta:
        model = Order
        # fields = ['id', 'waiterid', 'tableid', 'table_name', 'isitopen', 'total_sum', 'meals_id']
        fields = ['total_sum', 'meals_id', ]


class CheckSerializer(serializers.ModelSerializer):
    orderid = OrderSerializer2(read_only=True)
    orders_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source='orderid.id')

    class Meta:
        model = Check
        fields = ['id', 'orders_id', 'date', 'servicefree', 'orderid', ]


"""Create Check"""


class CheckSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ['id', 'date', 'servicefree', 'orderid']
