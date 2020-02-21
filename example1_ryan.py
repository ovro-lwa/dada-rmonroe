














#!/usr/bin/env python

from Dada import SortedDada

d = SortedDada("za_obs_0.dada")
d.setLineMappingFromFile("remap-danny2014.04.30.txt")

print "nAnt:", d.header.nAnt()
print "cFreq:", d.header.cFreq()
print "nFreq:", d.header.nFreq()

for vis in d:
	print vis.shape, vis[20000,52,0]
