# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0006_auto_20141004_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotacionConsejeroRegional',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('votos', models.IntegerField(default=0)),
                ('partido', models.ForeignKey(to='actas.Partido')),
                ('region', models.ForeignKey(to='actas.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VotacionPresidenteRegional',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('votos', models.IntegerField(default=0)),
                ('partido', models.ForeignKey(to='actas.Partido')),
                ('region', models.ForeignKey(to='actas.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='votacionregional',
            name='partido',
        ),
        migrations.RemoveField(
            model_name='votacionregional',
            name='region',
        ),
        migrations.DeleteModel(
            name='VotacionRegional',
        ),
        migrations.RenameField(
            model_name='actaregional',
            old_name='votos_blancos_reg',
            new_name='votos_blancos_cons',
        ),
        migrations.RenameField(
            model_name='actaregional',
            old_name='votos_emitidos_reg',
            new_name='votos_blancos_pres',
        ),
        migrations.RenameField(
            model_name='actaregional',
            old_name='votos_impugnados_reg',
            new_name='votos_emitidos_cons',
        ),
        migrations.RenameField(
            model_name='actaregional',
            old_name='votos_nulos_reg',
            new_name='votos_emitidos_pres',
        ),
        migrations.RenameField(
            model_name='detalleactaregional',
            old_name='votos_regional',
            new_name='votos_cons',
        ),
        migrations.AddField(
            model_name='actaregional',
            name='votos_impugnados_cons',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actaregional',
            name='votos_impugnados_pres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actaregional',
            name='votos_nulos_cons',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actaregional',
            name='votos_nulos_pres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalleactaregional',
            name='votos_pres',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
