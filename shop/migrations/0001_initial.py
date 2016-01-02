# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='이메일')),
                ('first_name', models.CharField(max_length=20, verbose_name='성')),
                ('last_name', models.CharField(max_length=20, verbose_name='이름')),
                ('joined_at', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='카테고리 이름')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200, verbose_name='이름')),
                ('desc', models.TextField(max_length=1000, verbose_name='설명')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('category', models.ForeignKey(to='shop.Category', verbose_name='카테고리')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPhoto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('image', models.ImageField(upload_to='%Y%m%d')),
                ('desc', models.TextField(max_length=500, verbose_name='사진설명')),
                ('item', models.ForeignKey(to='shop.Item')),
            ],
        ),
    ]
