# -*- coding: UTF-8 -*-
import os
import json
import urllib2
import csv
import configargparse

def main():
##ARGS
    parser = configargparse.ArgParser(description='geoFenceGen')
    parser.add_argument('-dir', '--directory', help='Directory and filename of geofence. ex: geofence/bratislava.txt', required=True)
    parser.add_argument('-l', '--location', help='City/Country/areas you wouls like the geofence for', required=True)
    args = parser.parse_args()
    wd = os.getcwd()
    end = "https://nominatim.openstreetmap.org/search.php?q='{}'&polygon_geojson=1&format=json".format(args.location)

## Get polygon
    raw = json.load(urllib2.urlopen(end))
    coords = [x for x in raw if x['osm_type'] == 'relation'][0]['geojson']['coordinates'][0]

##check if polygon is multipolygon


    print(len(coords[0]))

    if (len(coords[0]) == 2):
##Write fenceFile
        l = [["{}".format(args.location)]]
        with open('{}'.format(args.directory), 'wb') as f:

            writer = csv.writer(f)
            writer.writerow(l)
            for row in (coords):
                   writer.writerow(row[::-1])

        print("your geofence of {} has been created in: \n{}\{}".format(args.location,wd, args.directory))

    else:

        with open('{}'.format(args.directory), 'wb') as f:
            writer = csv.writer(f)
            for gf in (coords):
                n=0
                l = [["{}".format(args.location)]]

                for row in (coords [n]):
                    writer.writerow(l)
                    writer.writerow(row[::-1])
                n+=1


if __name__ == "__main__":
    main()