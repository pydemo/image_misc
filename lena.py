#lena test
from numpy import *
from pylab import *
from PIL import Image
from scipy import misc
im=misc.lena()
#figure()
#plot(im)
#contour( im, origin ='image') 
imshow(im)
show()