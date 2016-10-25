# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import csv
import json
import urllib
import sys, os

# input gps coords, function to use amap api to convert them to amap coords for further reverse Geocode
#  key is the amap developer key

def convert2amapcoord(lat, lon):
    urlparams = urllib.urlencode({'key': 'f9217d98e5e086977d7d2001157b3b1f',
                                  'locations': '{0},{1}'.format(lon, lat),
                                  'coordsys': 'gps'})
    url = 'http://restapi.amap.com/v3/assistant/coordinate/convert?' + urlparams
    urlhandler = urllib.urlopen(url)

    mdata = json.loads(urlhandler.read())
    coords = mdata['locations']
    lon_a, lat_a = coords.split(',')
    return lat_a, lon_a

#regeo nearest pois by input lat, lon
def regeo(lat, lon):
    urlparams = urllib.urlencode({'key': 'f9217d98e5e086977d7d2001157b3b1f',
                                  'location': '{0},{1}'.format(lon, lat),
                                  'poitype': '公司',
                                  'radius': 300,
                                  'extensions': 'all',
                                  'batch': 'false',
                                  'roadlevel': 1})
    url = 'http://restapi.amap.com/v3/geocode/regeo?' + urlparams
    urlhandler = urllib.urlopen(url)
    mdata = json.loads(urlhandler.read())
    addr = mdata['regeocode']['formatted_address']

    company = list()
    company.append(addr)

    note = 'there does not exist any companies near 300m of this coords'
    for poi in mdata['regeocode']['pois']:
        if u'公司' in poi['type']:
            company.append(poi['name'])
    if company:
        return company
    else:
        return note
        print note


if __name__ == '__main__':

    with open('gps_coords.csv', 'rb') as f:
        reader = csv.reader(f)
        gps = list(reader)

    # regeoresult_csv = file('regeo_result.csv', 'wb')
    regeoresult_csv = file('street_result.csv', 'wb')

    writer = csv.writer(regeoresult_csv, delimiter=';')
    i = 1
    size = len(gps[1:])
    for item in gps[1:]:
        lat = item[1]
        lon = item[2]
        lat_a, lon_a = convert2amapcoord(lat, lon)
        company = regeo(lat_a, lon_a)
        if isinstance(company, basestring):
            writer.writerow([''])
        else:
            writer.writerow([obs.encode('gbk') for obs in company])
        print '.....{0}/{1}.....'.format(i, size)
        i += 1

    regeoresult_csv.close()