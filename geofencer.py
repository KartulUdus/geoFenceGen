# -*- coding: UTF-8 -*-
import ujson
import urllib2
import csv
def main():

    raw = urllib2.urlopen("https://nominatim.openstreetmap.org/search.php?q='tartu'}&polygon_geojson=1&format=json").read()
    geojson = ujson.loads(raw)[0]['geojson']
    coords = geojson['coordinates']
    loc = (coords)[0]
    with open('output.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerow
        writer.writerows(loc)


if __name__ == "__main__":
    main()
