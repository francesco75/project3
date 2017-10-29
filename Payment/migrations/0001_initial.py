# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20170927_1526'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturePay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('ticket', models.ForeignKey(to='ticket.Ticket')),
                ('user', models.ForeignKey(related_name='payment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
