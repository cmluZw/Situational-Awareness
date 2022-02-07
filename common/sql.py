# config=utf-8
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO


def db_query(sql, settings=None, echo=None):

    if settings is None:
        settings = SQLALCHEMY_DATABASE_URI

    if echo is None:
        echo = SQLALCHEMY_ECHO

    return create_engine(settings, echo=echo).connect().execute(text(sql)).fetchall()


def db_execute(sql, settings=None, echo=None):

    if settings is None:
        settings = SQLALCHEMY_DATABASE_URI

    if echo is None:
        echo = SQLALCHEMY_ECHO

    return create_engine(settings, echo=echo).connect().execute(text(sql)).rowcount
