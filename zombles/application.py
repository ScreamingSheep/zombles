#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to respond to the request.
from webob import Request, Response


def application(environ, start_response):
    '''
    The main application.
    '''
    # Generate the request.
    request = Request(environ)

    # For testing, right now.
    response = Response()
    response.text = 'test'

    return response(environ, start_response)
