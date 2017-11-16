# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0003_remove_featurepay_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurepay',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
