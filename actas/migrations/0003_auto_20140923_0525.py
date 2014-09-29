# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0002_auto_20140923_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallediseñoacta',
            name='distrital',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='detallediseñoacta',
            name='provincial',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='detallediseñoacta',
            name='regional',
            field=models.BooleanField(default=False),
        ),
    ]
