import sys
import numpy as np
#>>> numbers = np.genfromtxt('text_file.txt', usecols=1 )
import random

import fileinput
from xml.dom import minidom


def read_file(fname):
	with open(fname, 'r') as file :
		filedata = file.read()

	filedata = filedata.replace(',', '.')

# Write the file out again
	with open(fname, 'w') as file:
		file.write(filedata)

	return np.genfromtxt(fname)

def plane_from_data(x):
	i1 = 1
	i2 = 2
	i3 = 3
	plane = np.cross( x[i1]-x[i2], x[i1]-x[i3] )
	plane = plane / np.linalg.norm(plane)
	return plane


if len(sys.argv)!=3:
    print("Usage: spread.py [ z_file.txt ] [ width ]")
    exit(1)
#print 'Number of arguments:', len(sys.argv), 'arguments.'

inFile = sys.argv[1]
width = float(sys.argv[2])






x = read_file(inFile)

plane = plane_from_data(x)
outFile = inFile.split(".")[0]+"_spread.txt"

of = open(outFile,"w") 

for d in x:
	v = d + plane * random.gauss(0,width)
	of.write(str(v[0]) + "\t" + str(v[1])   +"\t" +  str(v[2]) + "\n")


of.close()



