# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0007_auto_20141004_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votacionconsejeroregional',
            name='region',
        ),
        migrations.AddField(
            model_name='votacionconsejeroregional',
            name='provincia',
            field=models.ForeignKey(to='actas.Provincia', default=1),
            preserve_default=False,
        ),
    ]
