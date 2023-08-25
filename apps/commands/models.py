from django.db import models
from core.models import BaseModel


class QiqiCommandsCategoryModel(BaseModel):
    category_name = models.CharField(name='category_name', max_length=50)

    def __str__(self) -> str:
        return self.category_name
    

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class QiqiCommandsModel(BaseModel):
    command_name = models.CharField(name='command_name',max_length=50)
    command_mini_description = models.CharField(name='mini_description', null=True, max_length=100)
    command_description = models.TextField(name='command_description',null=True)
    command_how_to_use = models.CharField(name='command_use', max_length=256, null=True)
    command_example = models.CharField(name='command_example', null=True, max_length=256)
    command_category = models.ForeignKey(QiqiCommandsCategoryModel, models.CASCADE)


    def __str__(self):
        return self.command_name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

