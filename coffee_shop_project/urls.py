"""
URL configuration for coffee_shop_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from coffee_shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('coffeehouses/', CoffeeHouseList.as_view(), name='coffeehouse-list-create'),
    path('coffeehouses/<int:pk>/', CoffeeHouseDetail.as_view(), name='coffeehouse-detail'),

    path('menus/', MenuList.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),

    path('menuitems/', MenuItemList.as_view(), name='menuitem-list-create'),
    path('menuitems/<int:pk>/', MenuItemDetail.as_view(), name='menuitem-detail'),

    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
]
