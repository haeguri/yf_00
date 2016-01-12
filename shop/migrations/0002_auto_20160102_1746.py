# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.CommaSeparatedIntegerField(default=10000, max_length=10),
        ),
        migrations.AlterField(
            model_name='itemphoto',
            name='item',
            field=models.ForeignKey(related_name='photos_of_item', to='shop.Item'),
        ),
    ]
