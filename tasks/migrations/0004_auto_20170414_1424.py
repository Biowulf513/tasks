# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20170414_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(verbose_name='Автор задания', blank=True, related_name='task', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
