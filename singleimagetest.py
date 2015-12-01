from __future__ import division
import numpy as np
from scipy import ndimage as ndi

from skimage import feature
from scipy.misc import imread
from scipy.misc import imsave

#read image file to 2d array
filename = raw_input("Enter filename including extension: ")
im = imread("images/"+filename, flatten=True)

# Calculate area. The area we are interested in is the sum of the white pixels
area = (im>0).sum()
	
# Compute the Canny filter. This leaves only a white border around the shape.
edges = feature.canny(im, sigma=3.0)

#Calculate perimiter. The permiter we are interested in is the sum of the white pixels
#now that we've adjusted the image to be the white pixel border only
perimiter = (edges>0).sum() 

complexity = (perimiter * perimiter)/area

print "Area of " + str(filename) + " is " + str(area)
print "Perimeter of " + str(filename) + " is " + str(perimiter)
print "Complexity of " + str(filename) + " is " + str(complexity)
print complexity
print round(complexity)
	