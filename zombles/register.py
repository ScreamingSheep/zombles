#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to choose a spawn.
from random import choice

# Used to respond to the request.
from webob import Response

# Used to check for duplicate names.
from pymysql.err import IntegrityError


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
		
        # Make sure that there are spawn points.
        result = cursor.fetchall()
        if len(result) == 0:
            raise ValueError('You need to insert spawn points.')

        # Randomly choose a spawn point.
        return choice(result)

    finally:
        cursor.close()


def insert_user(connection, name, x, y):
    '''
    Creates the user.
    '''
    cursor = connection.cursor()

    try:
        cursor.execute('''
            INSERT INTO users (name, x, y)
            VALUES (%s, %s, %s)
        ''', [name, x, y])

    finally:
        cursor.close()


def register(request, connection):
    '''
    Used to register the user.
    '''
    # Get the name of the new user.
    name = request.json

    # Get the player's spawn.
    x, y = get_spawn(connection)
    
    # Create the response.
    response = Response()

    # Insert the player.
    try:
        insert_user(connection, name, x, y)
        
    except IntegrityError:
        response.text = 'Please try a different username.'
        
    else:
        response.text = 'Username successful!'

    return response