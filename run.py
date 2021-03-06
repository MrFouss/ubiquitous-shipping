#!/usr/bin/python3
# -*- coding: utf8 -*-

# File: run.py
#
# By Maxime Brodat <maxime.brodat@fouss.fr>
#
# Created: 17/04/2016 by Fouss

"""Running file for the transshipment solver project"""

from ag41_transshipment.app import Application
import sys
import os


def print_help(func_arg):
    """Displays the help of the program"""

    print('How to use:', file=sys.stderr)
    print('\t{} solve [data_file_name] [max_time]'.format(func_arg), file=sys.stderr)
    print('\t\tto solve the problem in the file [data_file_name] in maximum [max_time] milliseconds', file=sys.stderr)
    print('\t{} solve-all [data_directory] [max_time]'.format(func_arg), file=sys.stderr)
    print('\t\tto solve all problems in the folder [data_directory] in maximum [max_time] milliseconds', file=sys.stderr)
    print('\t{} clean [data_directory]'.format(func_arg), file=sys.stderr)
    print('\t\tto clean the folder [data_directory] of all .sol files', file=sys.stderr)


if len(sys.argv) == 4:
    if sys.argv[1] == 'solve':
        APP = Application(sys.argv[2], int(sys.argv[3]))

    elif sys.argv[1] == 'solve-all':
        files = os.listdir(sys.argv[2])
        files.sort()
        for file in files:
            parts = file.split('.')
            if 'sol' not in parts:
                APP = Application(sys.argv[2] + '/' + file, int(sys.argv[3]))
    else:
        print_help(sys.argv[0])

elif len(sys.argv) == 3:
    if sys.argv[1] == 'clean':
        files = os.listdir(sys.argv[2])
        nb_files = 0
        for file in files:
            parts = file.split('.')
            if 'sol' in parts:
                os.remove(sys.argv[2] + '/' + file)
                nb_files += 1
        print('All .sol files deleted!')
        print('{} files removed'.format(nb_files))
    else:
        print_help(sys.argv[0])

else:
    print_help(sys.argv[0])
