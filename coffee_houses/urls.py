from django.urls import path
from .views import CoffeeHouseList, CoffeeHouseDetail, MenuList, MenuDetail, MenuItemList, MenuItemDetail

urlpatterns = [
    path('coffeehouses/', CoffeeHouseList.as_view(), name='coffeehouse-list-create'),
    path('coffeehouses/<int:pk>/', CoffeeHouseDetail.as_view(), name='coffeehouse-detail'),

    path('menus/', MenuList.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),

    path('menuitems/', MenuItemList.as_view(), name='menuitem-list-create'),
    path('menuitems/<int:pk>/', MenuItemDetail.as_view(), name='menuitem-detail'),
]
