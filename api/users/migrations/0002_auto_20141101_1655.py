# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=b'', upload_to=b'avatars/', blank=True),
            preserve_default=True,
        ),
    ]
