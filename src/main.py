"""Main Executable Program File"""

import numpy as np
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from scipy import ndimage
import imageio.v3 as iio
import math

# TODO: Organize this into a more organized setup so work with audio and video is consistent 

def gaussian_filter(num_rows, num_cols, sigma):
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

def low_pass(image_matrix, sigma):
    frequency_domain = fftshift(fft2(image_matrix))

    filtered_frequencies = frequency_domain * gaussian_filter(image_matrix.shape[0], image_matrix.shape[1], sigma)
    
    return ifft2(ifftshift(filtered_frequencies))

def high_pass(image_matrix, sigma):
    frequency_domain = fftshift(fft2(image_matrix))

    # High frequency filter is same as 1 - low frequency filter
    filtered_frequencies = frequency_domain * (1 - gaussian_filter(image_matrix.shape[0], image_matrix.shape[1], sigma))

    return ifft2(ifftshift(filtered_frequencies))

def hybridImage(highFreqImg, lowFreqImg, sigmaHigh, sigmaLow):
    # TODO: Check for same image dimensions
    highPassed = high_pass(highFreqImg, sigmaHigh)
    lowPassed = low_pass(lowFreqImg, sigmaLow)
    return highPassed + lowPassed

if __name__ == "__main__":
    # Grayscale works.
    # TODO: Let's try RGB.
    # TODO: Let's try for Video.
    # TODO: Let's try for Music.
    # TODO: Let's write a really good explanation document.
    Ethan_Hunt = iio.imread("Ethan_Hunt.jpg")
    Ethan_Hunt = Ethan_Hunt[:, :, 0]
    James_Bond = iio.imread("James_Bond.jpg")
    James_Bond = James_Bond[:, :, 0]

    hybrid = hybridImage(James_Bond, Ethan_Hunt, 29, 14)
    hybrid = np.clip(np.abs(hybrid), 0, 255)
    iio.imwrite("combined.png", hybrid.astype(np.uint8))
    print("Done!")
