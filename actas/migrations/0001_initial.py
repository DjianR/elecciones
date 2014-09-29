# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('votos_blancos_reg', models.IntegerField()),
                ('votos_blancos_prov', models.IntegerField()),
                ('votos_blancos_dis', models.IntegerField()),
                ('votos_nulos_reg', models.IntegerField()),
                ('votos_nulos_prov', models.IntegerField()),
                ('votos_nulos_dis', models.IntegerField()),
                ('votos_impugnados_reg', models.IntegerField()),
                ('votos_impugnados_prov', models.IntegerField()),
                ('votos_impugnados_dis', models.IntegerField()),
                ('votos_emitidos_reg', models.IntegerField()),
                ('votos_emitidos_prov', models.IntegerField()),
                ('votos_emitidos_dis', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CentroVotacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleActa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('votos_regional', models.IntegerField()),
                ('votos_provincial', models.IntegerField()),
                ('votos_distrital', models.IntegerField()),
                ('acta', models.ForeignKey(to='actas.Acta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleDisenioActa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('distrital', models.BooleanField(default=False)),
                ('provincial', models.BooleanField(default=False)),
                ('regional', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisenioActa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=80)),
                ('capital_provincia', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('numero', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('total_electores', models.IntegerField()),
                ('procesada', models.BooleanField(default=False)),
                ('centro_votacion', models.ForeignKey(to='actas.CentroVotacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VotacionDistrital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('votos', models.IntegerField(default=0)),
                ('distrito', models.ForeignKey(to='actas.Distrito')),
                ('partido', models.ForeignKey(to='actas.Partido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VotacionProvincial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('votos', models.IntegerField(default=0)),
                ('partido', models.ForeignKey(to='actas.Partido')),
                ('provincia', models.ForeignKey(to='actas.Provincia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VotacionRegional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('votos', models.IntegerField(default=0)),
                ('partido', models.ForeignKey(to='actas.Partido')),
                ('region', models.ForeignKey(to='actas.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='provincia',
            name='region',
            field=models.ForeignKey(to='actas.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(to='actas.Provincia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disenioacta',
            name='distrito',
            field=models.ForeignKey(to='actas.Distrito'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalledisenioacta',
            name='disenio_acta',
            field=models.ForeignKey(to='actas.DisenioActa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalledisenioacta',
            name='partido',
            field=models.ForeignKey(to='actas.Partido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalleacta',
            name='partido',
            field=models.ForeignKey(to='actas.Partido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centrovotacion',
            name='distrito',
            field=models.ForeignKey(to='actas.Distrito'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acta',
            name='mesa',
            field=models.ForeignKey(to='actas.Mesa'),
            preserve_default=True,
        ),
    ]
