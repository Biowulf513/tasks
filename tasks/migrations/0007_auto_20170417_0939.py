# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20170414_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_photo',
            field=models.ImageField(upload_to='/task_photos/', verbose_name='фото', blank=True),
        ),
    ]
