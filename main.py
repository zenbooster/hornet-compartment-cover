#!/usr/bin/env python3
#coding: utf-8

from zencad import *

d = 5.9
w = 37.1
h = 19.9
t = 1.1

wh = w/2-h/2

A = (-h/2,-wh,0)
B = (-h/2,wh,0)
C = (0, w/2, 0)
D = (h/2,wh,0)
E = (h/2,-wh,0)
F = (0, -w/2, 0)

wire = sew([
    segment(A, B),
    circle_arc(B, C, D),
    segment(D, E),
    circle_arc(E, F, A),
])

m = wire.fill().extrude(t) - cylinder(d/2, t).forw(wh+0.5)

to_brep(m, 'hcc.brep')

disp(m)

show()
