#!/usr/bin/env python

# coding: utf-8

# In[86]:


import pandas # reading from csv file
import sys # to use constants declarared in the run.cmd
import os
import random
from PIL import Image, ImageDraw # this is used to draw circles
from os import path # this is used for VerifyInputs
import glob 


# constant declarations
PARAM_OUTPUT_IMAGE = 1
PARAM_X_SPACE = 2
PARAM_Y_SPACE = 3
PARAM_X_TRANS = 4
PARAM_Y_TRANS = 5

#define funtions

def VerifyInputs():
	if (len(sys.argv)!=6): # if the no. of arguments in the run.cmd file is not 8, print incorrect no. of parameters
		print("Incorrect number of parameters. ")
		print("Usage:") # define order of constants in run.cmd file
		print("python Overlay.py [ csv data ] [ png overlay input ] [ png output ] [ pixel separation x ] [ pixel separation y] [ pixel translation x] [ pixel translation y ]")
		exit(0)

def drawGridCrosses(img, dx, dy, tx, ty, size): # 8 arguments (input image, x spacing, y spacing, translation, cross size)
	draw = ImageDraw.Draw(img)

	rx = random.randint(0,dx)
	ry = random.randint(0,dy)

	for x in range(rx, int(img.width), int(dx)):
		for y in range(ry, int(img.height), int(dy)):
			draw.line((x-size, y, x+size, y), fill = (0,0,0), width = 1) 
			draw.line((x, y-size, x, y+size), fill = (0,0,0), width = 1)
  
#def findfile_paths(fileDirectory):
	#image_dir_list = []
	#for entry in os.scandir(fileDirectory):
	    #if (entry.path.endswith(".PNG")
	            #or entry.path.endswith(".png")) and entry.is_file():
	        	#image_dir_list.append(entry.path)
	#return image_dir_list

#listofImages = findfile_paths(r'C:\Users\sharoncy\Desktop\Programming\QC_mock_up_python\TestFolder')

def findImagesWithGlob(filedirectory):
	listofImages = []
	for imagepath in glob.iglob(filedirectory):
   		listofImages.append(imagepath)
	return listofImages

ImageList = findImagesWithGlob(r'C:\Users\sharoncy\Desktop\Programming\QC_mock_up_python\TestFolder\*.PNG')
output_png_filename = sys.argv[PARAM_OUTPUT_IMAGE]

for eachImage in ImageList:

#place output in an output directory
	tmpList = eachImage.split('\\')
	tempFilename = '\\'.join(tmpList[0:-1])
	newFilename = tempFilename + "\\output\\" + tmpList[-1]

#add _grid to output file name
	lst  = newFilename.split(".")
	newImageFilename = lst[0] + "_grid." + lst[1]
	print(newImageFilename)

# open image, apply grid and save in new directory with new name
	img = Image.open(eachImage)  
	drawGridCrosses(img, int(sys.argv[PARAM_X_SPACE]), int(sys.argv[PARAM_Y_SPACE]), int(sys.argv[PARAM_X_TRANS]),int(sys.argv[PARAM_Y_TRANS]), 8)
	img.save(newImageFilename) 


 














