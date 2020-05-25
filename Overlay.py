#!/usr/bin/env python

# coding: utf-8

# In[86]:


import pandas # reading from csv file
import sys # to use constants declarared in the run.cmd
import os.path
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


# define functions for this task: 1. VerifyInputs, 2. DrawGrid, 3. drawCircles, 4. drawDataCircles
# each function takes arguments. 
# some of the arguments are declared in the run.cmd file and pulled over by sys.argv
# run.cmd file: python Overlay.py Mock_up2.csv 132_CKT-2_110_NeuN_withRedGrid.png out 62 62 -10 10

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

def DrawGrid(img, col1, col2): # takes 3 arguments
	dy = int(sys.argv[PARAM_Y_SPACE]) #img1.height/NY (y_space is number of pixels between horizontal lines)
	NY = img.height/dy # total image height / desired y spacing
	dx = int(sys.argv[PARAM_X_SPACE]) #img1.height/NY (x_space is number of pixels between vertical lines)
	NX = img.width/dx # total image width / desired x spacing


	for y in range(1,int(NY)): # loop from 
		for x in range(0,img.width): # loop from 0 to full width of image
			img1.putpixel((x, int(y*dy)), col1)

	for x in range(1,int(NX)):
		for y in range(0,img.height): # loop through pixels from 0 to full height of image
			img.putpixel((int(x*dx), y), col2)


def drawCircles(img, dx,dy): # 3 arguments
	draw = ImageDraw.Draw(img)

	NX = int(img.width/dx) # image width / no. of pixels between vertical lines (62 in example)
	NY = int(img.height/dy) # image height / no. of pixels between horizontal lines (62 in example)

	size = img.width/NX/4

	for y in range(1, NY):	
		for x in range(1, NX):	
			cx = int(x*dx)
			cy = int(y*dy)

			draw.ellipse((cx-size, cy-size, cx+size, cy+size), fill = 'blue', outline ='black')

def drawDataCircles(img, dx, dy, tx, ty, d, size, column): # 8 arguments (input image, x spacing, y spacing, translation, circle size, csv column)
	draw = ImageDraw.Draw(img)

#	img.putalpha(128)
	values = d[column] # the values are pulled from the correct column
	xpos = d["Column "] #these are pulled from the csv file (column number)
	ypos = d["Row"] # these are pulled from the csv file (row number)
	colors = ['green', 'red', 'yellow'] # index 0, 1 and 2 = green, red and yellow respectively
	for i in range(0, len(values)):	# loop through from first row to last row in selected column
		x = int(xpos[i]) # x = all the x positions (pulled from the csv file)
		y = int(ypos[i]) # y = all the y position (pulled from the csv file)
		cx = int(x *dx) +tx # x position from csv * pixel spacing * x translation
		cy = int(y *dy) +ty # y position from csv * pixel spacing * y translation
		val = int(values[i]) # val = all the values in column
		#cx = int(x*dx)
		#cy = int(y*dy)

		draw.ellipse((cx-size, cy-size, cx+size, cy+size), fill = colors[val], outline ='black')

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
drawDataCircles(img1, int(sys.argv[PARAM_X_SPACE]),int(sys.argv[PARAM_Y_SPACE]), int(sys.argv[PARAM_X_TRANS]),int(sys.argv[PARAM_Y_TRANS]),data, 10, "ValueL")
img1.save(output_png_filename+"High.png") 

#drawDataCircles with argments from run.cmd. Data here is pulled from column "ValueH"
img1 = Image.open(input_png_filename)  
drawDataCircles(img1, int(sys.argv[PARAM_X_SPACE]),int(sys.argv[PARAM_Y_SPACE]), int(sys.argv[PARAM_X_TRANS]),int(sys.argv[PARAM_Y_TRANS]),data, 10, "ValueH")
img1.save(output_png_filename+"Low.png")  





