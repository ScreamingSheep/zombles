#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to choose a spawn.
from random import choice


def get_spawn(connection):
    '''
    Returns a random player spawn point as a tuple.
    '''
    cursor = connection.cursor()

    try:
        cursor.execute('''
            SELECT x, y
            FROM player_spawns
        ''')

    finally:
        cursor.close()

    return choice(cursor.fetchall())


def insert_user(connection, name, x, y):
    '''
    Creates the user.
    '''
    cursor = connection.cursor()

    try:
        cursor.execute('''
            INSERT INTO users (name, x, y)
            VALUES (%s, %s, %s)
        ''', name, x, y)

    finally:
        cursor.close()


def register(request, connection):
    '''
    Used to register the user.
    '''
    # Get the name of the new user.
    name = request.json

    # Get the player's spawn.
    x, y = get_spwan(connection)

    # Insert the player.
    insert_user(connection, name, x, y)
