# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170613_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.IntegerField(choices=[(2, 'Bank Disposal'), (1, 'Cash')], default=1),
        ),
    ]
