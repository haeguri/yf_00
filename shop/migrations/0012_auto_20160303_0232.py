# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20160226_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(default='B', choices=[('S', '박스 미개봉'), ('A', '거의 새것'), ('B', '사용감 있음'), ('C', '오래됨')], verbose_name='물품상태', max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CommaSeparatedIntegerField(default=10000, verbose_name='판매가', max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='shipping_price',
            field=models.CommaSeparatedIntegerField(null=True, verbose_name='배송료', max_length=10, blank=True),
        ),
    ]
