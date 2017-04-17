# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20170417_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_photo',
            field=models.ImageField(blank=True, upload_to='/tasks/static/tasks/update_photos/', verbose_name='фото'),
        ),
    ]
