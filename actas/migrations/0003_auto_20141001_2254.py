# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0002_auto_20141001_2229'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='detalleacta',
            unique_together=set([('acta', 'partido')]),
        ),
    ]
