# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20160115_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='include_shipping',
            field=models.BooleanField(verbose_name='배송료포함', default=False),
        ),
    ]
