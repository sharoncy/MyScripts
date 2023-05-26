#!/usr/bin/env python

# coding: utf-8

# In[86]:


import pandas # reading from csv file
import sys # to use constants declarared in the run.cmd
import os.path
import random
from PIL import Image, ImageDraw # this is used to draw circles
from os import path # this is used for VerifyInputs


# constant declarations
PARAM_CSV_FILE = 1
PARAM_INPUT_IMAGE = 2
PARAM_OUTPUT_IMAGE = 3
PARAM_X_SPACE = 4
PARAM_Y_SPACE = 5
PARAM_X_TRANS = 6
PARAM_Y_TRANS = 7

def VerifyInputs():
	if (len(sys.argv)!=8): # if the no. of arguments in the run.cmd file is not 8, print incorrect no. of parameters
		print("Incorrect number of parameters. ")
		print("Usage:") # define order of constants in run.cmd file
		print("python Overlay.py [ csv data ] [ png overlay input ] [ png output ] [ pixel separation x ] [ pixel separation y] [ pixel translation x] [ pixel translation y ]")
		exit(0)

	if (path.exists(sys.argv[PARAM_CSV_FILE])==False): # if CSV file does not exist
		print("Error : Could not find file '"+sys.argv[PARAM_CSV_FILE]+"'")
		exit(0)

	if (path.exists(sys.argv[PARAM_INPUT_IMAGE])==False): # if input image does not exist
		print("Error : Could not find image '"+sys.argv[PARAM_INPUT_IMAGE]+"'")
		exit(0)



def drawGridCrosses(img, dx, dy, tx, ty, d, size, column): # 8 arguments (input image, x spacing, y spacing, translation, circle size, csv column)
	draw = ImageDraw.Draw(img)

	rx = random.randint(0,dx)
	ry = random.randint(0,dy)

	for x in range(rx, int(img.width), int(dx)):
		for y in range(ry, int(img.height), int(dy)):
			draw.line((x-size, y, x+size, y), fill = (0,0,0), width = 1) 
			draw.line((x, y-size, x, y+size), fill = (0,0,0), width = 1)


# Call functions. In this case only VerifyInputs and drawDataCircles are called.  
VerifyInputs()

input_png_filename = sys.argv[PARAM_INPUT_IMAGE]
output_png_filename = sys.argv[PARAM_OUTPUT_IMAGE]

# Read data in csv file.
print("Loading csv file: " + sys.argv[PARAM_CSV_FILE])
data = pandas.read_csv(sys.argv[PARAM_CSV_FILE],delimiter=",")

#print(data)

# open the input image
img1 = Image.open(input_png_filename)  

#drawDataCircles with arguments from run.cmd. Data here is pulled from column "ValueL"
drawGridCrosses(img1, int(sys.argv[PARAM_X_SPACE]),int(sys.argv[PARAM_Y_SPACE]), int(sys.argv[PARAM_X_TRANS]),int(sys.argv[PARAM_Y_TRANS]),data, 8, "ValueL")
img1.save(output_png_filename+"GridCrosses.png") 












