# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('type', models.CharField(max_length=255)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('age_restricted', models.IntegerField(default=0)),
                ('text', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=255, unique=True, verbose_name='Ссылка на изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('type', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('coordinates_lt', models.FloatField(blank=True, null=True)),
                ('coordinates_lg', models.FloatField(blank=True, null=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='feed.City')),
                ('gallery', models.ManyToManyField(blank=True, related_name='places', to='feed.Gallery')),
                ('metros', models.ManyToManyField(blank=True, related_name='places', to='feed.Metro')),
                ('phones', models.ManyToManyField(blank=True, related_name='places', to='feed.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('time_till', models.DateTimeField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Event')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='worktime',
            unique_together=set([('time', 'type')]),
        ),
        migrations.AddField(
            model_name='place',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='places', to='feed.Tag'),
        ),
        migrations.AddField(
            model_name='place',
            name='work_times',
            field=models.ManyToManyField(blank=True, related_name='places', to='feed.WorkTime'),
        ),
        migrations.AlterUniqueTogether(
            name='phone',
            unique_together=set([('number', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('name', 'role')]),
        ),
        migrations.AddField(
            model_name='event',
            name='gallery',
            field=models.ManyToManyField(blank=True, related_name='events', to='feed.Gallery'),
        ),
        migrations.AddField(
            model_name='event',
            name='persons',
            field=models.ManyToManyField(blank=True, related_name='events', to='feed.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='events', to='feed.Tag'),
        ),
    ]
