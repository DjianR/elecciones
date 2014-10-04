# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0004_auto_20141003_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActaMunicipal',
            fields=[
                ('mesa', models.ForeignKey(to='actas.Mesa', primary_key=True, serialize=False)),
                ('votos_blancos_prov', models.IntegerField()),
                ('votos_blancos_dis', models.IntegerField()),
                ('votos_nulos_prov', models.IntegerField()),
                ('votos_nulos_dis', models.IntegerField()),
                ('votos_impugnados_prov', models.IntegerField()),
                ('votos_impugnados_dis', models.IntegerField()),
                ('votos_emitidos_prov', models.IntegerField()),
                ('votos_emitidos_dis', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActaRegional',
            fields=[
                ('mesa', models.ForeignKey(to='actas.Mesa', primary_key=True, serialize=False)),
                ('votos_blancos_reg', models.IntegerField()),
                ('votos_nulos_reg', models.IntegerField()),
                ('votos_impugnados_reg', models.IntegerField()),
                ('votos_emitidos_reg', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleActaMunicipal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('votos_provincial', models.IntegerField()),
                ('votos_distrital', models.IntegerField()),
                ('acta', models.ForeignKey(to='actas.ActaMunicipal')),
                ('partido', models.ForeignKey(to='actas.Partido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleActaRegional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('votos_regional', models.IntegerField()),
                ('acta', models.ForeignKey(to='actas.ActaRegional')),
                ('partido', models.ForeignKey(to='actas.Partido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleDisenioActaMunicipal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('distrital', models.BooleanField(default=False)),
                ('provincial', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleDisenioActaRegional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('regional', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisenioActaRegional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('region', models.ForeignKey(to='actas.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='DisenioActa',
            new_name='DisenioActaMunicipal',
        ),
        migrations.RemoveField(
            model_name='acta',
            name='mesa',
        ),
        migrations.AlterUniqueTogether(
            name='detalleacta',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='detalleacta',
            name='acta',
        ),
        migrations.DeleteModel(
            name='Acta',
        ),
        migrations.RemoveField(
            model_name='detalleacta',
            name='partido',
        ),
        migrations.DeleteModel(
            name='DetalleActa',
        ),
        migrations.RemoveField(
            model_name='detalledisenioacta',
            name='disenio_acta',
        ),
        migrations.RemoveField(
            model_name='detalledisenioacta',
            name='partido',
        ),
        migrations.DeleteModel(
            name='DetalleDisenioActa',
        ),
        migrations.AddField(
            model_name='detalledisenioactaregional',
            name='disenio_acta',
            field=models.ForeignKey(to='actas.DisenioActaRegional'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalledisenioactaregional',
            name='partido',
            field=models.ForeignKey(to='actas.Partido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalledisenioactamunicipal',
            name='disenio_acta',
            field=models.ForeignKey(to='actas.DisenioActaMunicipal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalledisenioactamunicipal',
            name='partido',
            field=models.ForeignKey(to='actas.Partido'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='detalleactaregional',
            unique_together=set([('acta', 'partido')]),
        ),
        migrations.AlterUniqueTogether(
            name='detalleactamunicipal',
            unique_together=set([('acta', 'partido')]),
        ),
        migrations.RenameField(
            model_name='mesa',
            old_name='procesada',
            new_name='procesada_municipal',
        ),
        migrations.AddField(
            model_name='mesa',
            name='procesada_regional',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
