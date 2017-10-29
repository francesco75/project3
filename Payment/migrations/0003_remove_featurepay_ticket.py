# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_featurepay_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurepay',
            name='ticket',
        ),
    ]
