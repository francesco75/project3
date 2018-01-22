# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0012_remove_vote_totalvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='user',
        ),
    ]
