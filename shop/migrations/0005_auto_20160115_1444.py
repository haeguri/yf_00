# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160112_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(),
        ),
    ]
