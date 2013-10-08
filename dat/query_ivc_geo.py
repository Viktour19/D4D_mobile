#!/usr/bin/python
# -*- coding: utf-8 -*-
##################Query the longitude and latitude for########################
###################all departments and regions in ivory coast##################
###############################################################################
from geocoder import geocode

infile = open("cities_departmentID.txt", "r")
all_lines = infile.readlines()
infile.close()

place_geo = {}
for line in all_lines:
    query = line.split()[-1]
    if query != 'NA' and query not in place_geo.keys():
        geo = geocode(query, site='bing')
        lon = str(geo['longitude'])
        lat = str(geo['latitude'])
        place_geo[query] = lon + ',' + lat
        print query, geo

write_lines = ['department\tlongitude\tlatitude\n']
for place, geo in place_geo.items():
    lon, lat = geo.split(',')
    newline = place + '\t' + lon + '\t' + lat + '\n'
    write_lines.append(newline)

outfile = open('ivc_dept_geo1.txt', 'w')
outfile.writelines(write_lines)
outfile.close()
