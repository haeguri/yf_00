# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20160212_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemphoto',
            name='desc',
        ),
    ]
