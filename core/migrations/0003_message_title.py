# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151025_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b'Mr.'), (1, b'Mrs.'), (2, b'Miss.'), (3, b'Dr.')]),
        ),
    ]
