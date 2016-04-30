# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20160310_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='credibility',
            field=models.CharField(choices=[('vendor', '거상'), ('pro', '프로'), ('newbie', '뉴비')], max_length=10, default='newbie'),
        ),
    ]
