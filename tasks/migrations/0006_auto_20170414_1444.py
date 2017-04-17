# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20170414_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_photo',
            field=models.ImageField(verbose_name='фото', upload_to='task_photos', blank=True),
        ),
    ]
