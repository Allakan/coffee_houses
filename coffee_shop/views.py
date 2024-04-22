from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import *
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.permissions import *


class CoffeeHouseList(ListCreateAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = [IsAuthenticated | IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CoffeeHouseDetail(RetrieveUpdateDestroyAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]


class MenuList(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated | IsAdminOrReadOnly]

    def perform_create(self, serializer):
        coffee_house_id = self.request.data.get('coffee_house')
        coffee_house = CoffeeHouse.objects.get(id=coffee_house_id)
        if coffee_house.owner == self.request.user:
            serializer.save(coffee_house=coffee_house)
        else:
            raise PermissionDenied("You do not have permission to create a menu for this coffee house.")


class MenuDetail(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]


class MenuItemList(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated | IsAdminOrReadOnly]

    def perform_create(self, serializer):
        menu_id = self.request.data.get('menu')
        menu = Menu.objects.get(id=menu_id)
        if menu.coffee_house.owner == self.request.user:
            serializer.save(menu=menu)
        else:
            raise PermissionDenied("You do not have permission to create a menu item for this menu.")


class MenuItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]