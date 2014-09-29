# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleDiseñoActa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('distrital', models.BooleanField()),
                ('provincial', models.BooleanField()),
                ('regional', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiseñoActa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('distrito', models.ForeignKey(to='actas.Distrito')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detallediseñoacta',
            name='diseño_acta',
            field=models.ForeignKey(to='actas.DiseñoActa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallediseñoacta',
            name='partido',
            field=models.ForeignKey(to='actas.Partido'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='acta_partido',
            name='jurisdiccion',
        ),
        migrations.DeleteModel(
            name='Jurisdiccion',
        ),
    ]
