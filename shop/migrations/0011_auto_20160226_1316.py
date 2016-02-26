# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_itemphoto_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(max_length=1000, default='이것은 설명입니다.'),
        ),
    ]
