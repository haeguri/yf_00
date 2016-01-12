# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20160112_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='credibility',
            field=models.CharField(choices=[('god', '신'), ('platinum', '플래티넘'), ('gold', '골드'), ('silver', '실버'), ('bronze', '브론즈')], default='bronze', max_length=10),
        ),
        migrations.AddField(
            model_name='item',
            name='vendor',
            field=models.ForeignKey(verbose_name='판매자', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
