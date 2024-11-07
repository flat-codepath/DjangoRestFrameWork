from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, ProductSerializer, CategorySerializer, LoginSerializer
from .models import Product, Category
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    DestroyAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# USER


class RetrieveCategory(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'name'


class ListCategory(APIView):
    # serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        categories_list = []
        for category in serializer.data:
            if category in categories_list:
                pass
            else:
                categories_list.append(category['name'])
        return Response(categories_list)


class UpdateCategory(RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'name'
    permission_classes = [IsAuthenticated]


class CreateCategory(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


class DeleteCategory(DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'name'
    permission_classes = [IsAuthenticated]


# PRODUCT RELATED

class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = [IsAuthenticated]


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class RetrieveProduct(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    # permission_classes = [IsAuthenticated]


class UpdateProduct(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class DeleteProduct(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    # permission_classes = [IsAuthenticated]


# class UserCreationApi(CreateAPIView):
#     serializer_class = UserRegisterSerializer
#     queryset = User

class UserRegisterApi(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'username': user.username,
                'data': {'data': 'user Created Successfully'}
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token = Token.objects.get_or_create(user=user)
                token_ticket = str(token)
                print(token)
                return Response({
                    'status': True,
                    'data': {'token': token_ticket}
                })
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'data': {},
                'message': "invalid credentials"
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors,
            'message': "invalid credentials"
        })
