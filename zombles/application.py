#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to respond to the request.
from webob import Request, Response

# Used to process requests.
from zombles.register import register

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
    }

    # Check for a bad path.
    if path not in api:
        response = HTTPNotFound
        return response(environ, start_response)

    try:
        # Connect to the database.
        connection = connect()

        # Generate the response.
        response = api[path](request, connection)

    except:
        response = HTTPInternalServerError()
        
    return response(environ, start_response)
