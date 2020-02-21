#!/usr/bin/env python

from Dada import SortedDada
from pyrap.tables import table

d = SortedDada("2014-04-30-01:21:56_0000536774737920.000000.dada")
d.setLineMappingFromFile("remap-danny2014.04.30.txt")

print "nAnt:", d.header.nAnt()
print "cFreq:", d.header.cFreq()
print "nFreq:", d.header.nFreq()

# Apply a CASA bandpass table
gain_tab = table('spw06.bcal', ack=False)
gains = gain_tab.getcol('CPARAM')
gain_flags = gain_tab.getcol('FLAG')
d.applyGains(gains, gain_flags)

for vis in d:
	print vis.shape, vis[20000,52,0]
