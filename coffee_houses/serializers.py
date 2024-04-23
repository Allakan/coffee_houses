from rest_framework import serializers
from .models import CoffeeHouse, Menu, MenuItem, Owner


class CoffeeHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeHouse
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'username', 'full_name', 'phone_number', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Пароль будет скрыт при выводе
        }

    def create(self, validated_data):
        user = Owner.objects.create_user(**validated_data)
        return user

