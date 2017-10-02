# -*- coding: UTF-8 -*-

import configargparse
import csv
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
from utils.args import get_args
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass







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
    file = open('utils/getGyms.sql', 'r')
    sql = " ".join(file.readlines())

    db = connect_db()
    cur = db.cursor()
    cur.execute(sql)
    coords = cur.fetchall()
    return coords
def cluster():


    coords = fetchGym()
    with open('gymgeofence.txt', 'wb') as f:
        writer = csv.writer(f)
        n=0
        for row in coords:
            l = [['gym']]
            writer.writerow(l)
            a=(coords[n][0] + 0.004,coords[n][1])
            b=(coords[n][0], coords[n][1] + 0.006)
            c=(coords[n][0] - 0.004, coords[n][1])
            d=(coords[n][0], coords[n][1] - 0.006)


            writer.writerow(a)
            writer.writerow(b)
            writer.writerow(c)
            writer.writerow(d)
            n+=1
if __name__ == "__main__":
    cluster()
