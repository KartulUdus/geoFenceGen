#!/usr/bin/python
# -*- coding: utf-8 -*-
import configargparse
import os
import sys
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

def get_args():
    # Get full dir and default config file path
    configfile = []
    if '-cf' not in sys.argv and '--config' not in sys.argv:
        configfile = [os.getenv('CONFIG', os.path.join(
            os.path.dirname(__file__), '../config/config.ini'))]
    parser = configargparse.ArgParser(
        default_config_files=configfile)

    # arrrgs, also available in config/config.ini


    parser.add_argument(
        '-cf',
        '--config', is_config_file=True,
        help='path to config file (config/config.ini by default)')

    parser.add_argument(
        '-H',
        '--host',
        help='mysql host'
        )
    parser.add_argument(
        '-u',
        '--user',
        help='mysql user'
        )
    parser.add_argument(
        '-pw',
        '--password',
        help='database password'
        )
    parser.add_argument(
        '-db',
        '--database',
        help='database name'
        )
    parser.add_argument(
        '-P',
        '--port',
        help='mysql port',
        default='3306')

    return parser.parse_args()