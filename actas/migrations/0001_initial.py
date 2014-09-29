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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('hora', models.TimeField()),
                ('votos_blancos', models.IntegerField()),
                ('votos_nulos', models.IntegerField()),
                ('votos_impugnados', models.IntegerField()),
                ('votos_emitidos', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Acta_Partido',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('votos_validos', models.IntegerField()),
                ('acta', models.ForeignKey(to='actas.Acta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CentroVotacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jurisdiccion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('distrital', models.BooleanField()),
                ('provincial', models.BooleanField()),
                ('regional', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('numero', models.CharField(max_length=6)),
                ('total_electores', models.IntegerField()),
                ('centro_votacion', models.ForeignKey(to='actas.CentroVotacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=80)),
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
            model_name='centrovotacion',
            name='distrito',
            field=models.ForeignKey(to='actas.Distrito'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acta_partido',
            name='jurisdiccion',
            field=models.ForeignKey(to='actas.Jurisdiccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acta_partido',
            name='partido',
            field=models.ForeignKey(to='actas.Partido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acta',
            name='mesa',
            field=models.ForeignKey(to='actas.Mesa'),
            preserve_default=True,
        ),
    ]
