#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to connect to the database.
import pymysql

# Connection parameters. This is very hacky!
from zombles.constants import HOST, PORT, DATABASE, USER, PASSWORD


def connect():
    '''
    A helper function to connect to the database.
    '''
    return pymysql.connect(host=HOST, port=PORT, user=USER, db=DATABASE,
						   passwd=PASSWORD)