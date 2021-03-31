from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    price = models.FloatField(
        verbose_name='Цена',
    )
    image = models.ImageField(
        verbose_name='Картинка',
    )

    def __str__(self):
        return self.title


class ResponseItem(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name='Имя',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    posted_time = models.DateTimeField(
        default=timezone.now,
        verbose_name='Время',
    )