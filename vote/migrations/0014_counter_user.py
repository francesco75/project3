# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_remove_ticket_totalvote'),
        ('vote', '0013_remove_counter_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='user',
            field=models.ForeignKey(to='ticket.Ticket'),
            preserve_default=False,
        ),
    ]
