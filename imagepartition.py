from __future__ import division
import numpy as np
import os
from scipy import ndimage as ndi
from skimage import feature
from scipy.misc import imread
from scipy.misc import imsave
import shutil

azcomplexity = []

#calculate complexity of letters a-z and store them in a list
for i in range(65,91):
	#read image file to 2d array
	filename = str(i)+".png"
	im = imread("az/"+filename, flatten=True)

	# Calculate area. The area we are interested in is the sum of the white pixels
	area = (im>0).sum()
	
	# Compute the Canny filter. This leaves only a white border around the shape.
	edges = feature.canny(im, sigma=3.0)

	#Calculate perimiter. The permiter we are interested in is the sum of the white pixels
	#now that we've adjusted the image to be the white pixel border only
	perimiter = (edges>0).sum() 
	
	complexity = (perimiter * perimiter)/area
	
	azcomplexity.append(int(round(complexity)))

#create folders a-z	
for i in range (0,26):
	directory = "images/" + str(chr(97+i))
	os.makedirs(directory)

#calculate complexity of each image and move it to relevant folder
for i in range(0,10000):
	#read image file to 2d array
	filename = str(i)+".png"
	im = imread("images/initial/"+filename, flatten=True)

	# Calculate area. The area we are interested in is the sum of the white pixels
	area = (im>0).sum()
	
	# Compute the Canny filter. This leaves only a white border around the shape.
	edges = feature.canny(im, sigma=3.0)

	#Calculate perimiter. The permiter we are interested in is the sum of the white pixels
	#now that we've adjusted the image to be the white pixel border only
	perimiter = (edges>0).sum() 
	
	if area > 1:
		complexity = (perimiter * perimiter)/area
		roundedcomplexity = int(round(complexity))
		print roundedcomplexity
		
		for x in xrange(len(azcomplexity)):
			if roundedcomplexity == azcomplexity[x]:
				shutil.copy("images/initial/"+filename,"images/"+str(chr(97+x)))
