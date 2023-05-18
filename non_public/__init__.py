from .keys import django_key
from .database import *
from collections import namedtuple


def django_key() -> str:
	return django_key


def database_params() -> namedtuple:
	params = namedtuple('DB_params', 'host user password db_name port')
	return params(host, user, password, db_name, port)
