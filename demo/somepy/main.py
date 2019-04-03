#!/bin/env python

import numpy
import imathnumpy
from imath import FloatArray, IntArray
import PyOpenColorIO as OCIO

length = 10
a = numpy.random.uniform(1,5,length)
b = numpy.random.uniform(1,5,length)
fdest = FloatArray(length)

dest = imathnumpy.arrayToNumpy(fdest)
dest[:] = a * b

results = fdest - a*b

print( "a: {}".format(a) )
print( "b: {}".format(b) )
print( "dest: {}".format(fdest) )
print( "diff: {}".format(results) )

config = OCIO.GetCurrentConfig()
print( "OCIO config: {}".format(config) )

