from django.db import models


"""Базовая модель. Абстрактный класс от которого наследуются все модели. Взял у Alenorze (никнейм человека на гитхабе)"""

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
