admin/ админ панель 

____________________________

coffeehouses/ кофейня

coffeehouses/<int:pk>/
____________________________

menus/ меню

menus/<int:pk>/

____________________________

menuitems/ пункты меню

menuitems/<int:pk>/

____________________________

auth/ авторизация
____________________________
Создание суперпользователя(админа) через терминал:

	python manage.py createsuperuser

Username - имя пользователя

Email address - почта

Password - пароль
