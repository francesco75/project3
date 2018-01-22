# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0007_remove_vote_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='totalvote',
            field=models.IntegerField(default=0),
        ),
    ]
