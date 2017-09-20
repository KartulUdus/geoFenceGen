# -*- coding: UTF-8 -*-

import configargparse
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint

def get_args():



def cluster():
    df = pd.read_csv('gymDumpRaw.csv')
    coords = df.as_matrix(columns=['lat', 'lon'])


def connect_db():

    try:
        args = get_args()
        return pymysql.connect(host="{}".format(
            args.host), port=int("{}".format(
                args.port)), user="{}".format(
            args.user), passwd="{}".format(
            args.password), database='{}'.format(args.database),
            connect_timeout=10)
    except pymysql.Error as e:
        sys.stderr.write("[ERROR] % d: % s\n" % (e.args[0], e.args[1]))
        return False

def fetchGym():

#Load the query
    file = open('utils/getGyms.sql' 'r')
    sql = " ".join(file.readlines())

#Dump the coords in csv file

    db = connect_db()
    dump_writer = csv.writer(
        open(
            'gymDumpRaw.csv',
            'w'),
        delimiter=',',
        quoting=csv.QUOTE_NONE)
    cur = db.cursor()
    cur.execute(sql)
    for row in cur.fetchall():
        dump_writer.writerow(row)
