# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0003_auto_20140923_0525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='id',
        ),
        migrations.AlterField(
            model_name='mesa',
            name='numero',
            field=models.CharField(serialize=False, primary_key=True, max_length=6),
        ),
    ]
