# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0008_votaciondistrital_votacionprovincial_votacionregional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votacionregional',
            name='votos',
            field=models.IntegerField(default=0),
        ),
    ]
