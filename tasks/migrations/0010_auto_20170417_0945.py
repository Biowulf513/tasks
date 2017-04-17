# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20170417_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_photo',
            field=models.ImageField(verbose_name='фото', upload_to='home/toor/django/tasks_django/tasks/static/tasks/update_photos/', blank=True),
        ),
    ]
