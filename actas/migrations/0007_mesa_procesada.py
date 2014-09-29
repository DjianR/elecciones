# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0006_auto_20140923_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='procesada',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
