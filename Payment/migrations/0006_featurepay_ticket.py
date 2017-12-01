# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20170927_1526'),
        ('Payment', '0005_featurepay_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurepay',
            name='ticket',
            field=models.ForeignKey(default=1, to='ticket.Ticket'),
            preserve_default=False,
        ),
    ]
