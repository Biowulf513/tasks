# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20170414_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_photo',
            field=models.ImageField(default='tasks/static/tasks/update_photos/image.jpg', upload_to='tasks/static/tasks/update_photos/', blank=True, verbose_name='фото'),
        ),
    ]
