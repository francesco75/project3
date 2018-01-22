# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0009_remove_vote_totalvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='totalvote',
            field=models.IntegerField(default=0),
        ),
    ]
