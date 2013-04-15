#!/usr/bin/env python
# coding: utf8
from sqlalchemy.pool import QueuePool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, exc
import models
import logger

engine = None
maker = None
BASE = models.BASE
log =None

def configure_db():
    global engine, session, log
    if not engine:
        engine = create_engine("mysql://root:feisky@10.241.226.41/news?charset=utf8",
            poolclass=QueuePool,
            echo_pool=True,
            pool_recycle=3600)
        register_models()
    log = logger.get_logger()
    log.info("db inited.")

def clear_db():
    global engine
    assert engine
    for table in reversed(BASE.metadata.sorted_tables):
        engine.execute(table.delete())


def register_models():
    """Register Models and create properties"""
    global engine
    assert engine
    BASE.metadata.create_all(engine)


def unregister_models():
    """Un register Models, useful clearing out data before testing"""
    global engine
    assert engine
    BASE.metadata.drop_all(engine)


def get_session(autocommit=True, expire_on_commit=False):
    """Helper method to grab session"""
    global maker, engine
    if not maker:
        assert engine
        maker = sessionmaker(bind=engine,
            autocommit=autocommit,
            expire_on_commit=expire_on_commit)
    return maker()


def news_create(title, url, site, **kwargs):
    session = get_session()
    with session.begin():
        news = models.News(title, url, site)
        for key in kwargs.keys():
            news[key] = kwargs[key]
        session.add(news)
        session.flush()
        return news


def news_list(page_size, page=0, filters=None):
    log.info("Listing news ...")
    session = get_session()
    query = session.query(models.News)
    if filters:
        query = query.filter(filters)
        query.limit(page_size)
    query = query.limit(page_size)
    query = query.offset(page * page_size)
    return query.all()


def news_get(id):
    session = get_session()
    return session.query(models.News).filter_by(id=id).one()


def news_update(id, **kwargs):
    session = get_session()
    news = news_get(id)
    if not news:
        return None
    for key in kwargs.keys():
        news[key] = kwargs[key]
    session.merge(news)
    session.flush()
    return news


def news_destroy(id):
    session = get_session()
    try:
        news = session.query(models.News).filter_by(id=id).one()
        session.delete(news)
        session.flush()
    except:
        raise Exception("News %d not found" % id)


if __name__ == '__main__':
    configure_db()
    import time
    while True:
        news = news_list(20)
        for n in news:
            print n.title, n.url
        print news_get(2534).title
        news = news_create("test tile", "http://www.test.com", "test")
        print news_get(news.id)
        news = news_update(news.id, abstract="This is a test")
        print news
        news_destroy(news.id)
        time.sleep(0.1)
