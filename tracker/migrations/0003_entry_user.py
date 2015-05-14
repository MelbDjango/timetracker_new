# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def set_entry_user(apps, schema_editor):
    Entry = apps.get_model('tracker', 'Entry')
    User = apps.get_model('auth', 'User')

    u = User.objects.first()

    for entry in Entry.objects.all():
        entry.user = u
        entry.save()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0002_auto_20150402_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.RunPython(set_entry_user),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
