#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to access console parameters.
from sys import argv


def main():
    '''
    Runs the main server.
    '''
    # Print usage.
    if len(argv) != 3:
        print('Usage: zombles host port')

    # Get the server's parameters.
    host = argv[1]
    port = int(argv[2])

    # Create the server.
    print('Listening on %s:%d' % (host, port))
    server = make_server(host, port, application)
    server.serve_forever()
