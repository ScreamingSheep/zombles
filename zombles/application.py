#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to respond to the request.
from webob import Request, Response

# Used to process requests.
from zombles.register import register
from zombles.move import move

# Exception handling.
from webob.exc import HTTPInternalServerError, HTTPNotFound

# Database connection.
from zombles.database import connect


def application(environ, start_response):
    '''
    The main application.
    '''
    # Generate the request.
    request = Request(environ)
    path = request.path_info_pop()

    # API end points.
    api = {
        'register': register,
        'move': move,
    }

    # Check for a bad path.
    if path not in api:
        response = HTTPNotFound()
        return response(environ, start_response)

    # Connect to the database.
    connection = connect()

    try:
        # Generate the response.
        response = api[path](request, connection)

    except:
        # If something went wrong, undo any changes.
        connection.rollback()
        raise
        
    else:
        # If things go okay, write stuff to the database.
        connection.commit()
        
    finally:
        # Close the connection so that someone else can use it.
        connection.close()
        
    return response(environ, start_response)