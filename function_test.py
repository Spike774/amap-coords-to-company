# -*- coding: UTF-8 -*-
import json
import csv

# with open('test_gps.json', 'rb') as f:
#     mdata = json.load(f)
#     coords = mdata['locations']
#     lon, lat = coords.split(',')
#     print 'Here is the jsonfile {0}, \nHere is the coords {1},\nHere is the lon {2} and lat {3}'.format(mdata, coords, lon, lat)

# with open('test_regeo_json.json', 'rb') as f:
#     mdata = json.load(f)
#     # coords = mdata['locations']
#     # lon, lat = coords.split(',')
#     # print 'Here is the jsonfile {0}, \nHere is the coords {1},\nHere is the lon {2} and lat {3}'.format(mdata, coords, lon, lat)
#     company = list()
#     for poi in mdata['regeocode']['pois']:
#         if u'公司' in poi['type']:
#             company.append(poi['name'])
#
#     print company
#     # print mdata['regeocode']['pois'][0]['name']

u'\u82cf\u95fd(\u5f20\u5bb6\u6e2f)\u65b0\u578b\u91d1\u5c5e\u6750\u6599\u79d1\u6280\u6709\u9650\u516c\u53f8'

with open('regeo_result_test.csv', 'wb') as f:
    writer = csv.writer(f, delimiter = ';')
    writer.writerow([])