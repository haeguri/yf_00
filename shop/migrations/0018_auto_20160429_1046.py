# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20160429_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='state',
            field=models.CharField(default='sale', max_length=4, choices=[('sold', '판매완료'), ('sale', '판매중')], verbose_name='판매여부'),
        ),
    ]
