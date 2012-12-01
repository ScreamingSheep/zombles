#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to access console parameters.
from sys import argv

# Used to connect to the server.
from requests import post

# Used to encode the request.
from json import loads, dumps


def register(url):
    '''
    Used to register the user.
    '''
    # Get the user's name.
    name = input('Please enter your name: ')

    # Register the user.
    response = post(url + 'register', data=dumps(name))
    id = loads(response.text)
    
    return id

def get_move():
    '''
    Used to get the move from the user.
    '''
    move = None
    while True:
        # Get a movement.
        move = input('Enter move: ')
        
        # Check to see if it's valid.
        if move in ['w', 'a', 's', 'd']:
            break
    
    return move
    
def move(url, user_id, the_move):
    '''
    Sends the movement to the server.
    '''
    # Create the move data.
    data = {
        'user': user_id,
        'move': the_move,
    }
    
    # Try to move player.
    response = post(url + 'move', data=dumps(data))
    print(response.text)
    
def main():
    '''
    Runs the client.
    '''
    # Print usage.
    if len(argv) != 3:
        print('Usage: zombles host port')

    # Get the server's parameters.
    host = argv[1]
    port = int(argv[2])
    url = 'http://%s:%d/' % (host, port)

    # Register the new user.
    user_id = register(url)
    
    while True:
        # Get the move from the player.
        the_move = get_move()
        move(url, user_id, the_move)