# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0005_auto_20141004_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalledisenioactaregional',
            old_name='regional',
            new_name='consejero',
        ),
        migrations.AddField(
            model_name='detalledisenioactaregional',
            name='presidente',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
