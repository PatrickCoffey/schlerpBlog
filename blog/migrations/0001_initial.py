# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.TextField(default=b'Anonymous', max_length=100, verbose_name=b'Author')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'Publish Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=300, verbose_name=b'Post Title')),
                ('author', models.TextField(default=b'Schlerp', max_length=100, verbose_name=b'Author')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'Publishing Date')),
                ('text', models.TextField(verbose_name=b'Body')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
            preserve_default=True,
        ),
    ]
