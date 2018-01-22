# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20170927_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='type',
            field=models.CharField(default=((b'bug', b'bug'), (b'feature', b'feature')), max_length=254, choices=[(b'bug', b'bug'), (b'feature', b'feature')]),
        ),
    ]
