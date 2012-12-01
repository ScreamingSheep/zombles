#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to respond to the request.
from webob import Response

# Used Json to encode the result
from json import dumps

def get_xy(connection, user_id):
    '''
    Gets coordinates of player
    '''
    cursor = connection.cursor()

    try:
        cursor.execute('''
            select x, y
            from users
            where id=%s
        ''', [user_id])
		
        # Returns result
        result = cursor.fetchone()
        return result

    finally:
        cursor.close()

def update(the_move, x, y):
    '''
    Applies the move to the current x and y and returns a new x and y.
    '''
    if the_move == 'w':
        return x, y+1
    elif the_move == 's':
        return x, y-1
    elif the_move == 'a':
        return x-1, y
    else:
        return x+1, y
        
def set_xy(connection, user_id, x, y):
    '''
    Sets coordinates of player
    '''
    cursor = connection.cursor()

    try:
        cursor.execute('''
           update users 
           set x=%s,y=%s 
           where id=%s
        ''', [x, y, user_id])

    finally:
        cursor.close()
        
def move(request, connection):
    '''
    Used to move the user.
    '''
    # Get the name of the new user.
    data = request.json
    user_id = data['user']
    the_move = data['move']
    
    x, y = get_xy(connection, user_id)
    x, y = update(the_move, x, y)
    
    set_xy(connection, user_id, x, y)
    
    # Create the response.
    response = Response()
    response.json = x, y
    
    return response