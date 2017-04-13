# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя категории транслитом')),
                ('title', models.CharField(max_length=50, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категоия',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя тега транслитом')),
                ('title', models.CharField(max_length=50, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название задачи')),
                ('description', models.TextField(verbose_name='Описание')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, verbose_name='Сроки задачи')),
                ('rate', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('category', models.ForeignKey(verbose_name='Категоия', to='tasks.Category', related_name='task')),
                ('tag', models.ManyToManyField(related_name='task', verbose_name='Тэги', to='tasks.Tag')),
                ('user', models.ForeignKey(verbose_name='Автор задания', to=settings.AUTH_USER_MODEL, related_name='task')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
