# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurepay',
            name='name',
            field=models.CharField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
