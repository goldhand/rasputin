# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_id', models.CharField(max_length=200, blank=True)),
                ('sample_name', models.CharField(max_length=200, blank=True)),
                ('test_id', models.CharField(max_length=200, blank=True)),
                ('sample_type', models.CharField(max_length=200, blank=True)),
                ('batch', models.CharField(max_length=200, blank=True)),
                ('units', models.CharField(max_length=2, choices=[(b'mg', b'Millagrams'), (b'pc', b'Percent')])),
                ('test_date', models.DateTimeField(null=True, blank=True)),
                ('thc', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('thc_a', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('thc_v', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('cbd', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('cbd_a', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('cbd_v', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('cbc', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('cbg', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('cbn', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('max_thc', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('max_cbd', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('total_active', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('total_cannabinoids', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
