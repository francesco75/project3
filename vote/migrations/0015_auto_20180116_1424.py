# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0014_counter_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='user',
        ),
        migrations.DeleteModel(
            name='Counter',
        ),
    ]
