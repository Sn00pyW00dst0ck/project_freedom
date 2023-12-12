import numpy as np
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from scipy import ndimage

# TODO: Add support for RGB

class Image_Filterer:

    def __init__(self):
        pass

    def apply_filter(self, image_matrix, method, *params):
        # List out supported method names and their associated application functions
        methods = {
            'low_pass': self.__apply_low_pass_filter, 
            'high_pass': self.__apply_high_pass_filter, 
            'gaussian': self.__apply_gaussian_filter, 
            'average': self.__apply_average_filter
        }

        # Check for valid method, call the method if it is valid
        if method not in methods:
            raise ValueError("Invalid method")
        
        return methods[method](image_matrix, params)

    # Function to apply specific filters (for internal use only)

    def __apply_average_filter(self, image_matrix, filter_size):
        # filter size is a tuple (rows, cols)
        return image_matrix * self.__get_average_filter(filter_size[0], filter_size[1])

    def __apply_gaussian_filter(self, image_matrix, filter_size, sigma):
        # filter size is a tuple (rows, cols)
        # sigma is a number
        return image_matrix * self.__get_gausian_filter(filter_size[0], filter_size[1], sigma)
    
    def __apply_low_pass_filter(self, image_matrix, sigma):
        frequency_domain = fftshift(fft2(image_matrix))
        filtered_frequencies = frequency_domain * self.__get_gaussian_filter(image_matrix.shape[0], image_matrix.shape[1], sigma[0])
        return ifft2(ifftshift(filtered_frequencies))
    
    def __apply_high_pass_filter(self, image_matrix, sigma):
        frequency_domain = fftshift(fft2(image_matrix))
        # High frequency filter is same as 1 - low frequency filter
        filtered_frequencies = frequency_domain * (1 - self.__get_gaussian_filter(image_matrix.shape[0], image_matrix.shape[1], sigma[0]))
        return ifft2(ifftshift(filtered_frequencies))

    # Functions to generate filters (for internal use only)

    def __get_average_filter(self, num_rows, num_cols):
        # Get a filter used for averaging
        filter_array = np.ones((num_rows, num_cols))
        filter_array = filter_array / filter_array.size
        return filter_array
    
    def __get_gaussian_filter(self, num_rows, num_cols, sigma):
        # These are used to center the filter
        center_row = num_rows // 2
        center_col = num_cols // 2

        # Originally I had a separate function to calculate the Gaussian filter at each point and
        # would loop over each position in the filter and calculate the Gaussian at that point, 
        # but using np.ogrid is shorter and more numpy friendly, at the cost of readability.

        # Using ogrid to get arrays of coordinates for fast processing with numpy
        i, j = np.ogrid[:num_rows, :num_cols]
        # Apply the formula from https://en.wikipedia.org/wiki/Gaussian_filter to every position in the filter
        filter_array = np.exp(-((i - center_row) ** 2 + (j - center_col) ** 2) / (2 * sigma ** 2)) 
        # Return the made filter
        return filter_array
    
    # Other filter types here
