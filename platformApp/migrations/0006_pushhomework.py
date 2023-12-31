# Generated by Django 4.1.3 on 2022-11-08 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('platformApp', '0005_gradehomework'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushHomework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.FileField(upload_to='materials/homeWorks', verbose_name='Файл')),
                ('homeWork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platformApp.homework', verbose_name='Задание #')),
            ],
            options={
                'verbose_name': 'Отправленная работы',
                'verbose_name_plural': 'Отправленные работы',
            },
        ),
    ]
