#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to respond to the request.
from webob import Response

# Used Json to encode the result
from json import dumps

def move(request, connection):
    '''
    Used to move the user.
    '''
    # Get the name of the new user.
    data = request.json
    
    # Create the response.
    response = Response()
    response.text = 'hello'
    
    return response