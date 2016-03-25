# -*- coding: utf-8 -*-
from django.db import models


class Gallery(models.Model):
    image_url = models.URLField(max_length=255, verbose_name='Ссылка на изображение', unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Metro(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Person(models.Model):
    role = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = (
            ('name', 'role',)
        )


class Phone(models.Model):
    type = models.CharField(max_length=255)
    number = models.BigIntegerField()

    class Meta:
        unique_together = (
            ('number', 'type')
        )


class WorkTime(models.Model):
    type = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    class Meta:
        unique_together = (
            ('time', 'type')
        )


class Event(models.Model):
    event_id = models.IntegerField(default=0)
    title = models.CharField(verbose_name='Название', max_length=255)
    type = models.CharField(max_length=255)
    runtime = models.IntegerField(null=True, blank=True)
    age_restricted = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True, related_name='events')
    gallery = models.ManyToManyField(Gallery, blank=True, related_name='events')
    persons = models.ManyToManyField(Person, blank=True, related_name='events')
    text = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Place(models.Model):
    place_id = models.IntegerField(default=0)
    title = models.CharField(verbose_name='Название', max_length=255)
    type = models.CharField(max_length=255)
    address = models.CharField(null=True, blank=True, max_length=255)
    coordinates_lt = models.FloatField(null=True, blank=True)
    coordinates_lg = models.FloatField(null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    city = models.ForeignKey(City, related_name='places', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='places')
    metros = models.ManyToManyField(Metro, blank=True, related_name='places')
    work_times = models.ManyToManyField(WorkTime, blank=True, related_name='places')
    gallery = models.ManyToManyField(Gallery, blank=True, related_name='places')
    phones = models.ManyToManyField(Phone, blank=True, related_name='places')
    text = models.TextField(null=True, blank=True)


class Schedule(models.Model):
    date = models.DateField()
    time = models.DateTimeField()
    event = models.ManyToManyField(Event, blank=True)
    place = models.ManyToManyField(Place, blank=True)
    time_till = models.DateTimeField(null=True, blank=True)
