#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to access console parameters.
from sys import argv

# Used to connect to the server.
from requests import post

# Used to encode the request.
from json import dumps


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
    url = 'http://%s:%d/register' % (host, port)

    # Register the user.
    name = dumps('victor')
    response = post(url, data=name)
    print(response.text)
