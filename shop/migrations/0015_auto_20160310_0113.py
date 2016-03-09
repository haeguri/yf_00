# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_item_purchased_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='state',
            field=models.CharField(choices=[('sale', '판매중'), ('sold', '판매완료')], max_length=4, verbose_name='판매여부', default='sale'),
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(max_length=1000, verbose_name='설명'),
        ),
    ]
