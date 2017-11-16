# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_vote_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='published_date',
        ),
    ]
