#!/usr/bin/python
# Filename: cartesian_dist.py
""" Python module for determining distance between two coordinate locations
in the 3-D cartesian space. The two points are (x1,y1,z1) and (x2,y2,z2). """

from math import sqrt

def dist(pnts):

    x1 = pnts[0]
    y1 = pnts[1]
    z1 = pnts[2]
    x2 = pnts[3]
    y2 = pnts[4]
    z2 = pnts[5]

    d = sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

    return d
