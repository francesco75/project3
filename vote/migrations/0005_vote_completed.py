# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20170913_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
