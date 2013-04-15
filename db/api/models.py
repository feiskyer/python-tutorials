#!/usr/bin/env python
# coding: utf8
# https://github.com/xinnet-iaas-openstack/quantum/blob/master/quantum/db/api.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relation, object_mapper

BASE = declarative_base()


class NewsBase(object):
    """Base class for News Models."""

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __iter__(self):
        self._i = iter(object_mapper(self).columns)
        return self

    def next(self):
        n = self._i.next().name
        return n, getattr(self, n)

    def update(self, values):
        """Make the model object behave like a dict"""
        for k, v in values.iteritems():
            setattr(self, k, v)

    def iteritems(self):
        """Make the model object behave like a dict.
        Includes attributes from joins."""
        local = dict(self)
        joined = dict([(k, v) for k, v in self.__dict__.iteritems()
                       if not k[0] == '_'])
        local.update(joined)
        return local.iteritems()


class News(BASE, NewsBase):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(512))
    url = Column(String(128))
    site = Column(String(256))
    abstract = Column(String(2048))
    created = Column(DateTime)
    file = Column(String(128))

    def __init__(self, title, url, site):
        self.title = title
        self.url = url
        self.site = site

    def __repr__(self):
        return "[%s] %s (via %s)" % (self.title, self.abstract, self.url)