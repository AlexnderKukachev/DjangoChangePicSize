# DjangoService
Этот сервис позволяет загружать свои изображения с компьютера, либо по URL адресу и изменять его размер.
Размер меняется визуально(без сохранения), оригинал изображения при этом сохраняетя.

Для запуска проекта:
1. Скачайте репозиторий ветви master
2. Установите Python 3 
3. Запустите виртуальное окружение

3.1. В случаи если виртуальное окружение не заработает удалите папку venv

3.2. Выполните команду python -m venv venv из папки djangotesttask

3.3. Установите Django 3, модули Pillow, requests

4. В консоли перейдите в папку djangotesttask\DjangoTestTask и выполните команды python manage.py makemigrations за ней python manage.py migrate
5. Для запуска сервера Django в папке djangotesttask\DjangoTestTask выполните команду python manage.py runserver
