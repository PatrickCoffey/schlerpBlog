# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.TextField(max_length=100, verbose_name='Media Title'),
        ),
        migrations.AlterField(
            model_name='media',
            name='upload',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
