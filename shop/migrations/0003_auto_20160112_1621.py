# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160102_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.CharField(max_length=1, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], verbose_name='물품상태', default='B'),
        ),
        migrations.AddField(
            model_name='item',
            name='deal_place',
            field=models.CharField(null=True, max_length=10, verbose_name='거래장소', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='deal_way',
            field=models.CharField(max_length=6, choices=[('direct', '직거래'), ('ship', '택배'), ('delivery', '직접배달')], verbose_name='거래방법', default='direct'),
        ),
        migrations.AddField(
            model_name='item',
            name='purchased_at',
            field=models.CharField(max_length=10, verbose_name='구입일', default='거래장소'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='shipping_price',
            field=models.CharField(null=True, max_length=10, verbose_name='배송료', blank=True),
        ),
    ]
