from PIL import Image 
from numpy import * 
im = array( Image.open('C:\Users\Public\Pictures\Sample Pictures\Desert.jpg'). convert('L')) 
im2, cdf = histeq( im)

iml=('C:\Users\Public\Pictures\Sample Pictures\Desert.jpg', 'C:\Users\Public\Pictures\Sample Pictures\Koala.jpg')

im5=compute_average(iml)
im6=Image.fromarray(im5)
contour( im5, origin ='image') 
axis('equal') 
axis('off')
show()

