# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20170908_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thread',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
