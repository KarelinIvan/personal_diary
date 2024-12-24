from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Электронная почта', help_text='Укажите e-mail')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', help_text='Укажите номер телефона',
                             **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', help_text='Укажите город')
    avatar = models.ImageField(upload_to='users/media', verbose_name='Аватар', help_text='Загружите фото', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
