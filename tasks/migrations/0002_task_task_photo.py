# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_photo',
            field=models.ImageField(blank=True, default='tasks/static/task_photos/image.jpg', upload_to='task_photos', verbose_name='фото'),
        ),
    ]
