# -*- coding: UTF-8 -*-
import json
import urllib2
import csv
import configargparse


def main():

    # ARGS
    parser = configargparse.ArgParser(description='geoFenceGen')
    parser.add_argument(
        '-dir',
        '--directory',
        help='Directory and filename of geofence. ex: geofence/bratislava.txt',
        required=True)
    parser.add_argument(
        '-l',
        '--location',
        help='City/Country/areas you wouls like the geofence for',
        required=True)
    parser.add_argument(
        '-w',
        '--way',
        help=('Use if there\'s no relational polygon'),
        action='store_true',
        default=False)
    parser.add_argument(
        '-mp',
        '--multi-polygon',
        help=('Use if you wish to write all polygons of an area'),
        action='store_true',
        default=False)

    args = parser.parse_args()
    end = "https://nominatim.openstreetmap.org/search.php?q='{}'&polygon_geojson=1&format=json".format(
        args.location)

# Get polygon
    raw = json.load(urllib2.urlopen(end))
    coords = [x for x in raw if x['osm_type'] ==
              'relation'][0]['geojson']['coordinates']

# check if polygon is multipolygon

    print(len(coords[0][0]))

    if (len(coords[0][0]) == 2):
        # Write fenceFile
        l = [["{}".format(args.location)]]
        with open('{}'.format(args.directory), 'wb') as f:

            writer = csv.writer(f)
            writer.writerow(l)
            for row in (coords[0]):
                writer.writerow(row[::-1])

        print(
            "your geofence of {} has been created in: {}".format(
                args.location,
                args.directory))

    else:
        # Write fenceFile
        with open('{}'.format(args.directory), 'wb') as f:
            writer = csv.writer(f)
            for z in (coords):
                n = 0
                l = [["{}{}".format(args.location, n + 1)]]
                writer.writerow(l)
                for row in (coords[0][n]):
                    writer.writerow(row[::-1])
                n += 1
            print(
                "Multiplygon geofence of {} has been created in: {}".format(
                    args.location, args.directory))


if __name__ == "__main__":
    main()
