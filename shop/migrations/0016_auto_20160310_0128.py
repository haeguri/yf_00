# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20160310_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('body', models.CharField(verbose_name='코멘트', max_length=300)),
                ('created_at', models.DateTimeField(verbose_name='등록일', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='수정일', auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='item',
            name='shipping_price',
        ),
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(verbose_name='물품상태', choices=[('S', '아직 미개봉'), ('A', '거의 새것'), ('B', '사용감 있음'), ('C', '오래됨')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='deal_way',
            field=models.CharField(verbose_name='거래방법', choices=[('direct', '직거래'), ('ship', '택배')], default='direct', max_length=6),
        ),
        migrations.AddField(
            model_name='itemcomment',
            name='item',
            field=models.ForeignKey(related_name='comments', to='shop.Item'),
        ),
        migrations.AddField(
            model_name='itemcomment',
            name='user',
            field=models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
