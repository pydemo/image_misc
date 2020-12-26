from PIL import Image 
from pylab import * 
# read image to array 
im = array( Image.open('C:\Users\Public\Pictures\Sample Pictures\Desert.jpg'). convert('L')) 
# create a new figure figure() 
# don't use colors 
gray() 
# show contours with origin upper left corner 
im = array( Image.open(' empire.jpg').convert(' L')) 
contour( im, origin ='image') 
axis('equal') 
axis('off')
show()
im2 = 255 - im # inverts image
contour( im2, origin ='image') 
show()
# invert image 
im3 = (100.0/ 255) * im + 500 #clamps the intensities to the interval 100 . . . 200,


contour( im3, origin ='image') 
show()
# clamp to interval 100... 200 
im4 = 255.0 * (im/ 255.0)** 2 # squared, which lowers the values of the darker pixels.


contour( im4, origin ='image') 
show()

