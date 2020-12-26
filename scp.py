from PIL import Image 
from numpy import * 
from scipy.ndimage import filters 
im = array( Image.open('C:\Users\Public\Pictures\Sample Pictures\Desert.jpg'). convert(' L')) 
im2 = filters.gaussian_filter( im, 5)
#contour( im2, origin ='image') 
#axis('equal') 
#axis('off')
show(im2)

