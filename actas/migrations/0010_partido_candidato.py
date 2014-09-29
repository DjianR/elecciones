# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0009_auto_20140924_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='candidato',
            field=models.CharField(default=datetime.date(2014, 9, 24), max_length=150),
            preserve_default=False,
        ),
    ]
