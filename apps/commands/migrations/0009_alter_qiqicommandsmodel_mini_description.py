# Generated by Django 4.2.3 on 2023-08-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0008_rename_commandscategorymodel_qiqicommandscategorymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qiqicommandsmodel',
            name='mini_description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
