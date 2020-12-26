def histeq( im, nbr_bins = 256): 
	""" Histogram equalization of a grayscale image. """
	# get image histogram 
	imhist, bins = histogram( im.flatten(), nbr_bins, normed = True) 
	cdf = imhist.cumsum() 
	# cumulative distribution function cdf = 255 * cdf / cdf[-1] 
	# normalize 
	# use linear interpolation of cdf to find new pixel values 
	im2 = interp( im.flatten(), bins[:-1], cdf) 
	return im2.reshape( im.shape), cdf
	
def compute_average( imlist): 
	""" Compute the average of a list of images. """ 
	# open first image and make into array of type float 
	averageim = array( Image.open( imlist[ 0]), 'f') 
	for imname in imlist[ 1:]: 		
		averageim = averageim+array( Image.open( imname))
	averageim = averageim/len( imlist) 
	# return average as uint8 
	#return array( averageim, 'uint8')
	return averageim



