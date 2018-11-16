# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 14:14
from __future__ import unicode_literals

import article.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('is_public', models.BooleanField(default=True, verbose_name='公开')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to=article.models.article_img_path, verbose_name='展示图')),
                ('tags', models.CharField(blank=True, help_text='用空格分隔', max_length=200, null=True, verbose_name='标签')),
                ('summary', models.TextField(verbose_name='摘要')),
                ('content', models.TextField(verbose_name='正文')),
                ('view_times', models.IntegerField(default=0, verbose_name='查看次数')),
                ('zan_times', models.IntegerField(default=0, verbose_name='点赞次数')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿')], default=0, verbose_name='状态')),
                ('is_abandon', models.BooleanField(default=False, verbose_name='是否删除')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
                'ordering': ['-is_top', '-view_times', '-publish_time'],
                'permissions': (('view_article', '查看所有文章'),),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_article', to='article.Article', verbose_name='文章')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Comment', verbose_name='引用')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
