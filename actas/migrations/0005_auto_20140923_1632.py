# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0004_auto_20140923_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleActa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('votos_regional', models.IntegerField()),
                ('votos_provincial', models.IntegerField()),
                ('votos_distrital', models.IntegerField()),
                ('acta', models.ForeignKey(to='actas.Acta')),
                ('partido', models.ForeignKey(to='actas.Partido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='acta_partido',
            name='acta',
        ),
        migrations.RemoveField(
            model_name='acta_partido',
            name='partido',
        ),
        migrations.DeleteModel(
            name='Acta_Partido',
        ),
        migrations.RemoveField(
            model_name='acta',
            name='hora',
        ),
        migrations.AddField(
            model_name='distrito',
            name='capital_provincia',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
