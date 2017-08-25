# -*- coding: UTF-8 -*-
import os
import ujson
import urllib2
import csv
import configargparse
def main():

    parser = configargparse.ArgParser(description='geoFenceGen')
    parser.add_argument('-dir', '--directory', help='Directory and filename of geofence. ex: geofence/bratislava.txt', required=True)
    parser.add_argument('-l', '--location', help='City/Country/areas you wouls like the geofence for', required=True)
    args = parser.parse_args()
    wd = os.getcwd()
    end = "https://nominatim.openstreetmap.org/search.php?q='{}'&polygon_geojson=1&format=json".format(args.location)
    raw = urllib2.urlopen(end).read()
    geojson = ujson.loads(raw)[0]['geojson']
    coords = geojson['coordinates']
    loc = (coords)[0]
    l = [["{}".format(args.location)]]
    with open('{}'.format(args.directory), 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(l)
        writer.writerows(loc)

    print("your geofence of {} has been created in: \n{}\{}".format(args.location,wd, args.directory))

if __name__ == "__main__":
    main()
