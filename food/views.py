from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, permissions
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework import exceptions
from rest_framework import generics

from food import models
from food import serializers as ser

"""User by using base way"""


class UserListView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserListSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        seria = UserDetailSerializer(user, data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data)
        return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""MEAL by Using mixins"""


class MealListView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MealDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""Table  by Using generic class-based views"""


class TableList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Table.objects.all()
    serializer_class = TableListSerializer


class TableDetail(generics.RetrieveDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableDetailSerializer


"""Role"""


class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleListSerializer


class RoleDetail(generics.RetrieveDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleDetailSerializer


"""Department"""


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer


class DepartmentDetail(generics.RetrieveDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentDetailSerializer


"""MealCategory"""


class MealCategoryList(generics.ListCreateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategoryListSerializer


class MealCategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategoryDetailSerializer


"""MealCategoriesByDepartment"""


class MealCategoriesByDepartmentList(generics.ListCreateAPIView):
    queryset = MealCategoriesByDepartment.objects.all()
    serializer_class = MealCategoriesByDepartmentListSerializer


"""MealCategory"""


class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusListSerializer


class StatusDetail(generics.RetrieveDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusDetailSerializer


"""MealCategory"""


class ServicePercentageList(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageListSerializer


class ServicePercentageDetail(generics.RetrieveDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageDetailSerializer


"""MealCategory"""


class MealsToOrderList(generics.ListCreateAPIView):
    queryset = MealsToOrder.objects.all()
    serializer_class = MealsToOrderSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CheckList(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class CheckList2(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer2


###############################################
class MethodSerializerView(object):
    '''
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('GET', ): MyModelListViewSerializer,
        ('PUT', 'PATCH'): MyModelCreateUpdateSerializer
    }
    '''
    method_serializer_classes = None

    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
                'Expected view %s should contain method_serializer_classes '
                'to get right serializer class.' %
                (self.__class__.__name__,)
        )
        for methods, serializer_cls in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)


class CheckListCreateView(MethodSerializerView, generics.ListCreateAPIView):

    '''
    API: /users
    Method: GET/POST
    '''
    queryset = models.Check.objects.all()
    method_serializer_classes = {
        ('GET',): ser.CheckSerializer,
        ('POST'): ser.CheckSerializer2
    }


#############################


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class ActiveOrder(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.filter(isitopen=True)
