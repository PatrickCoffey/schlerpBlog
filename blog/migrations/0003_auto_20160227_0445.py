# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160226_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.TextField(default='Anonymous', verbose_name='Author', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Publish Date', auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(default='Schlerp', verbose_name='Author', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Publishing Date', auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(verbose_name='Post Title', max_length=300),
        ),
    ]
