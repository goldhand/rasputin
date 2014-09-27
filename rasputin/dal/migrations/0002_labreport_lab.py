# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
        ('dal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labreport',
            name='lab',
            field=models.ForeignKey(default=1, to='labs.Lab'),
            preserve_default=False,
        ),
    ]
