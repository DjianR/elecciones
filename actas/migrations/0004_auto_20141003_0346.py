# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0003_auto_20141001_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acta',
            name='votos_blancos_reg',
        ),
        migrations.RemoveField(
            model_name='acta',
            name='votos_emitidos_reg',
        ),
        migrations.RemoveField(
            model_name='acta',
            name='votos_impugnados_reg',
        ),
        migrations.RemoveField(
            model_name='acta',
            name='votos_nulos_reg',
        ),
        migrations.RemoveField(
            model_name='detalleacta',
            name='votos_regional',
        ),
        migrations.RemoveField(
            model_name='detalledisenioacta',
            name='regional',
        ),
    ]
