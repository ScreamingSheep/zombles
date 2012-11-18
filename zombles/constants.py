#!/usr/bin/python
# -*- coding: utf-8 -*-

# The database connection parameters.
HOST = 'localhost'
PORT = 3306
DATABASE = 'zombles'
# The root user is used to void the hasstle of setting up a user in mysql.
USER = 'root'
PASSWORD = 'vgss'

# To prevent the user from having to type a lot of choices out, we can use
# these dictionaries to translate back and fourth between shortcuts.
CHOICES = {
    'left': 'left(a)',
    'right': 'right(d)',
    'up': 'forward(w)',
    'down': 'back(s)',
    'pick up': 'pick up(e)',
    'drop': 'drop(q)',
    'exit': 'exit(x)',
}

# The reverse mapping.
SHORTCUTS = {
    'a': 'left',
    'd': 'right',
    'w': 'up',
    's': 'down',
    'e': 'pick up',
    'q': 'drop',
    'x': 'exit',
}