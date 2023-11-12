from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    is_active = models.BooleanField(verbose_name='активность', default=True)
    telegram = models.CharField(max_length=50, verbose_name='телеграм', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
