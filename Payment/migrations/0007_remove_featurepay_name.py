# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0006_featurepay_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurepay',
            name='name',
        ),
    ]
