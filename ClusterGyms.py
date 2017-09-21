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

#Dump the coords in csv file

    db = connect_db()
    dump_writer = csv.writer(
        open(
            'gymDumpRaw.csv',
            'w'),
        delimiter=',',
        quoting=3)
    cur = db.cursor()
    cur.execute(sql)
    for row in cur.fetchall():
        dump_writer.writerow(row)

def cluster():
    df = pd.read_csv('gymDumpRaw.csv')
    coords = df.as_matrix(columns=['lat', 'lon'])

    print df

    # kms_per_radian = 6371.0088
    # epsilon = 1.5 / kms_per_radian
    # db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='precomputed').fit(np.radians(coords))
    # cluster_labels = db.labels_
    # num_clusters = len(set(cluster_labels))
    # clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
    # print('Number of clusters: {}'.format(num_clusters))


if __name__ == "__main__":
    cluster()
