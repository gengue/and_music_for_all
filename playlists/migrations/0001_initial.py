# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('category', models.ForeignKey(to='playlists.Category')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de modificacion')),
                ('url', models.CharField(max_length=500)),
                ('media_type', models.CharField(max_length=255, choices=[(b'YOUTUBE', b'YOUTUBE'), (b'SOUNCLOUD', b'SOUNDCLOUD'), (b'VIMEO', b'VIMEO')])),
                ('playlist', models.ForeignKey(to='playlists.Playlist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
