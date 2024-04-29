from rest_framework import serializers
from .models import CoffeeHouse, Menu, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, required=False)

    class Meta:
        model = Menu
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        items_info = Menu.objects.create(**validated_data)
        for item_data in items_data:
            Menu.objects.create(menu_items_info=items_info, **item_data)
        return items_info


class CoffeeHouseSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, required=False)

    class Meta:
        model = CoffeeHouse
        fields = '__all__'

    def create(self, validated_data):
        menus_data = validated_data.pop('menus', [])
        menus_info = CoffeeHouse.objects.create(**validated_data)
        for menu_data in menus_data:
            CoffeeHouse.objects.create(menus_info=menus_info, **menu_data)
        return menus_info