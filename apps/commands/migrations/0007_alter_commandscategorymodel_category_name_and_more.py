# Generated by Django 4.2.3 on 2023-08-23 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0006_alter_commandscategorymodel_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandscategorymodel',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='qiqicommandsmodel',
            name='command_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commands.commandscategorymodel'),
        ),
    ]
