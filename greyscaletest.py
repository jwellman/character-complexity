import pylab as pl
import matplotlib.cm as cm
import numpy as np
from PIL import Image

im = Image.open('Screenshot.png')
im_grey = im.convert('L') # convert the image to *greyscale*
im_array = np.array(im_grey)
pl.imshow(im_array, cmap=cm.Greys_r)
pl.show() 