# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160227_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=100, verbose_name=b'Media Title')),
                ('upload', models.FileField(upload_to=b'uploads/')),
                ('slug', models.SlugField(unique=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
