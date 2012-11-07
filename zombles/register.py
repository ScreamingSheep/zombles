#!/usr/bin/python
# -*- coding: utf-8 -*-


def register(request, connection):
    '''
    Used to register the user.
    '''
    # Get the name of the new user.
    name = request.json
