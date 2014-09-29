# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0005_auto_20140923_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acta',
            old_name='votos_blancos',
            new_name='votos_blancos_dis',
        ),
        migrations.RenameField(
            model_name='acta',
            old_name='votos_emitidos',
            new_name='votos_blancos_prov',
        ),
        migrations.RenameField(
            model_name='acta',
            old_name='votos_impugnados',
            new_name='votos_blancos_reg',
        ),
        migrations.RenameField(
            model_name='acta',
            old_name='votos_nulos',
            new_name='votos_emitidos_dis',
        ),
        migrations.AddField(
            model_name='acta',
            name='votos_emitidos_prov',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acta',
            name='votos_emitidos_reg',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acta',
            name='votos_impugnados_dis',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acta',
            name='votos_impugnados_prov',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acta',
            name='votos_impugnados_reg',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acta',
            name='votos_nulos_dis',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acta',
            name='votos_nulos_prov',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acta',
            name='votos_nulos_reg',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
