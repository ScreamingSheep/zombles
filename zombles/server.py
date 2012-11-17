#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to run the wsgiref server.
from wsgiref.simple_server import make_server

# Used to access console parameters.
from sys import argv

# The application.
from zombles.application import application


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


# Start the server if the script is called directly.
if __name__ == '__main__':
	main()