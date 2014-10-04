# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acta',
            name='id',
        ),
        migrations.AlterField(
            model_name='acta',
            name='mesa',
            field=models.ForeignKey(serialize=False, to='actas.Mesa', primary_key=True),
        ),
    ]
