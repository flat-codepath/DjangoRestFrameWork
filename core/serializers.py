from .models import Category, Product
from django.contrib.auth.models import User
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name','password']
#
#         def create(self, **validated_data):
#             user=User.objects.create_user(validated_data)
#             return user
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create a user with the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'] or None,
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'stock_quantity', 'price', 'description', 'category']
