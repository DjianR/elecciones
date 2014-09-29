# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0007_mesa_procesada'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotacionDistrital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('votos', models.IntegerField()),
                ('partido', models.ForeignKey(to='actas.Partido')),
                ('region', models.ForeignKey(to='actas.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
