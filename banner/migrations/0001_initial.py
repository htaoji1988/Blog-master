# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 14:14
from __future__ import unicode_literals

import banner.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='摘要')),
                ('img', models.FileField(upload_to=banner.models.carousel_img_path, verbose_name='轮播图片')),
                ('img_xs', models.FileField(upload_to=banner.models.carousel_img_path, verbose_name='手机轮播图片')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='文章')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'ordering': ['-create_time'],
            },
        ),
    ]
