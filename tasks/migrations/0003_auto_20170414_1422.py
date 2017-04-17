# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_task_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tag',
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Сроки задачи'),
        ),
    ]
