# -*- coding: utf-8 -*-
from django.db import models


class Author(models.Model):
    name = models.CharField('Name', null=True, blank=True, max_length=255)

    def __unicode__(self):
        return self.name


class SortableBook(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    my_order = models.PositiveIntegerField(blank=False, null=False)
    author = models.ForeignKey(Author, null=True)

    class Meta(object):
        ordering = ('my_order',)

    def __unicode__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    book = models.ForeignKey(SortableBook, null=True)
    my_order = models.PositiveIntegerField(blank=False, null=False)

    class Meta(object):
        ordering = ('my_order',)

    def __unicode__(self):
        return u'Chapter: %s' % self.title
