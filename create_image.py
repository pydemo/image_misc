from numpy import * 
from numpy import random 
from scipy.ndimage import filters 
import rof 
# create synthetic image with noise 
im = zeros(( 500,500)) 
im[ 100: 400,100: 400] = 128 
im[ 200: 300,200: 300] = 255 
im = im + 30* random.standard_normal(( 500,500))
imshow(im)
show()
G = filters.gaussian_filter(im,10)
imshow(G)
show()


