# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_remove_ticket_totalvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(default=((b'To Do', b'To Do'), (b'Doing', b'Doing'), (b'Done', b'Done')), max_length=254, choices=[(b'To Do', b'To Do'), (b'Doing', b'Doing'), (b'Done', b'Done')]),
        ),
    ]
