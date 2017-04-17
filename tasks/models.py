from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Имя категории транслитом', max_length=50)
    title = models.CharField('Название категории', max_length=50)

    class Meta:
        verbose_name = 'Категоия'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField('Имя тега транслитом', max_length=50)
    title = models.CharField('Название тега', max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField('Название задачи', max_length=50)
    description = models.TextField('Описание')
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    end_date = models.DateTimeField('Сроки задачи', blank=True, null=True)
    user = models.ForeignKey(User, related_name='task', verbose_name='Автор задания',
                             blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name='task', verbose_name='Категоия')
    # tag = models.ManyToManyField(
    #     Tag, related_name='task', verbose_name='Тэги')
    rate = models.IntegerField('Рейтинг', default=0)

    task_photo = models.ImageField(
        'фото', upload_to='home/toor/django/tasks_django/tasks/static/tasks/update_photos/',blank=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
