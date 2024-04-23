from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings


class Owner(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email', 'phone_number']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='owner_set',  # Изменяем related_name для groups
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='owner_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.full_name


class CoffeeHouse(models.Model):
    name = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='coffee_houses')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    coffee_house = models.ForeignKey(CoffeeHouse, on_delete=models.CASCADE, related_name='menus')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    VOLUME_UNITS = (
        ('ml', 'мл'),
        ('l', 'л'),
        ('g', 'г'),
        ('kg', 'кг'),
    )

    name = models.CharField(max_length=255)
    volume_or_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_of_measurement = models.CharField(max_length=2, choices=VOLUME_UNITS)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    photo = models.ImageField(upload_to='menu_items/', blank=True, null=True)

    def __str__(self):
        return self.name
