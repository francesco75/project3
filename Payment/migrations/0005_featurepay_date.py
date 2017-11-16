# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0004_featurepay_is_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurepay',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 17, 24, 45, 698000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
