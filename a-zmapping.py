import numpy as np
from scipy import ndimage as ndi

from skimage import feature
from scipy.misc import imread
from scipy.misc import imsave

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
	
	print "Complexity for " + str(i) + " is " + str(complexity)