# Generated by Django 4.2.3 on 2023-08-22 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_qiqicommandsmodel_mini_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QiqiCommandsModel',
        ),
    ]