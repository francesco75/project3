# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_vote_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
