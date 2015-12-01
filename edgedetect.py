import numpy as np
from scipy import ndimage as ndi

from skimage import feature
from scipy.misc import imread
from scipy.misc import imsave

#read image file to 2d array
im = imread("whitesquare.png", flatten=True)

# Print area. The area we are interested in is the sum of the white pixels
print "Area:",(im>0).sum()

# Compute the Canny filter. This leaves only a white border around the shape.
edges = feature.canny(im, sigma=3.0)

#Print perimiter. The permiter we are interested in is the sum of the white pixels
#now that we've adjusted the image to be the white pixel border only
print "perimeter: ",(edges>0).sum() 

#save output image to file
imsave('output.png', edges)

#use wolfram imagelevels for comparisons
#p^2/A