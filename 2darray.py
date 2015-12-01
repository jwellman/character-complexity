from PIL import Image
from numpy import*

temp=asarray(Image.open('blackwhite.png'))
for j in temp:
    new_temp = asarray([[i[0],i[1]] for i in j]) # new_temp gets the two first pixel values

print temp
print temp.shape