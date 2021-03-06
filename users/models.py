from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

