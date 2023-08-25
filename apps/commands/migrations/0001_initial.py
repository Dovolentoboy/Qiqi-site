# Generated by Django 4.2.4 on 2023-08-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QiqiCommandsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('command_name', models.CharField(max_length=50)),
                ('mini-description', models.CharField(max_length=24, null=True)),
                ('command_description', models.TextField(null=True)),
                ('command_use', models.CharField(max_length=256, null=True)),
                ('command_example', models.CharField(max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
    ]
