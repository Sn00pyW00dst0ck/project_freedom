import numpy as np
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from scipy import ndimage

import imageio.v3 as iio
import pygame
from pygame.locals import QUIT



class Image_Processor:
    """
    A class for easily working with RGB images.
    Provides methods for loading images, 
    saving images to a file, and performing
    basic operations on images.
    """

    image_data = None

    def __init__(self):
        pass

    def load_from_file(self, file_path):
        """
        Loads an image from a file. Can be greyscale or RGB.

        Args:
            file_path (string):
                The path from which to load the image data.
        """
        self.image_data = iio.imread(file_path)

    def load_from_data(self, image_data):
        """
        Loads an image from data. Can be greyscale or RGB.

        Args:
            image_data (pygame.Surface):
                The image data to load.
        """
        self.image_data = image_data
    
    def display_image(self):
        """
        Displays the loaded image data in a pygame window!
        The image data can be RGB or grayscale.
        """
        pygame.init()

        # The transpose is needed due to coordinate differences in pygame and numpy
        image_surface = pygame.surfarray.make_surface(np.transpose(self.image_data, axes=(1,0,2)))
        screen = pygame.display.set_mode((self.image_data.shape[1], self.image_data.shape[0]))

        # Constantly need to check if user has closed the window or not!
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return

            # Display the image on the screen
            screen.blit(image_surface, (0, 0))
            pygame.display.flip()

    def save_to_file(self, file_path):
        """
        Save an image from the loaded data.

        Args:
            file_path (string):
                The file to save the image to.
        """
        iio.imwrite(file_path, self.image_data.astype(np.uint8))


    def custom_hybridization(self, other, sigma_high, sigma_low):
        """
        Perform a custom image hybridization by merging the high 
        frequency portion of one image with the low frequency 
        portion of another image.

        Args:
            other (Image_Processor):
                An Image_Processor containing the loaded image to use
                for the low frequency image.
            
            sigma_high (float):

            sigma_low (float):

        """
        highPassed = self.apply_filter('high_pass', sigma_high)
        lowPassed = other.apply_filter('low_pass', sigma_low)
        self.image_data = np.clip(np.abs(highPassed + lowPassed), 0, 255)



    def apply_filter(self, method, *params):
        """
        Apply a filter to the currently loaded image data.

        There are 4 supported filter types:
            low_pass
            high_pass
            gaussian
            average
        
        Args:
            method (string):
                One of the four supported filter types, as a string.
            
            *params:
                The parameters necessary to apply the selected filter.
        """
        methods = {
            'low_pass': self.__apply_low_pass_filter, 
            'high_pass': self.__apply_high_pass_filter, 
            'gaussian': self.__apply_gaussian_filter, 
            'average': self.__apply_average_filter
        }

        if method not in methods:
            raise ValueError("Invalid method")
        
        return methods[method](params)

    def __apply_average_filter(self, filter_size):
        return self.image_data * self.__get_average_filter(filter_size[0], filter_size[1])

    def __apply_gaussian_filter(self, filter_size, sigma):
        return self.image_data * self.__get_gaussian_filter(filter_size[0], filter_size[1], sigma)
    
    def __apply_low_pass_filter(self, sigma):
        # Handle grayscale
        if self.image_data.ndim == 2:
            frequency_domain = fftshift(fft2(self.image_data))
            filtered_frequencies = frequency_domain * self.__get_gaussian_filter(self.image_data.shape[0], self.image_data.shape[1], sigma[0])
            return ifft2(ifftshift(filtered_frequencies))

        # Handle RGB in separate channels
        filtered_channels = []
        for channel in range(self.image_data.shape[2]):
            frequency_domain = fftshift(fft2(self.image_data[:,:,channel]))
            filtered_frequencies = frequency_domain * self.__get_gaussian_filter(self.image_data.shape[0], self.image_data.shape[1], sigma[0])
            filtered_channels.append(ifft2(ifftshift(filtered_frequencies)))
        return np.stack(filtered_channels, axis=2)
    
    def __apply_high_pass_filter(self, sigma):
        # Handle grayscale
        if self.image_data.ndim == 2:
            frequency_domain = fftshift(fft2(self.image_data))
            # High frequency filter is same as 1 - low frequency filter
            filtered_frequencies = frequency_domain * (1 - self.__get_gaussian_filter(self.image_data.shape[0], self.image_data.shape[1], sigma[0]))
            return ifft2(ifftshift(filtered_frequencies))

        # Handle RGB in separate channels
        filtered_channels = []
        for channel in range(self.image_data.shape[2]):
            frequency_domain = fftshift(fft2(self.image_data[:,:,channel]))
            # High frequency filter is same as 1 - low frequency filter
            filtered_frequencies = frequency_domain * (1 - self.__get_gaussian_filter(self.image_data.shape[0], self.image_data.shape[1], sigma[0]))
            filtered_channels.append(ifft2(ifftshift(filtered_frequencies)))
        return np.stack(filtered_channels, axis=2)

    def __get_average_filter(self, num_rows, num_cols):
        filter_array = np.ones((num_rows, num_cols))
        filter_array = filter_array / filter_array.size
        return filter_array
    
    def __get_gaussian_filter(self, num_rows, num_cols, sigma):
        center_row = num_rows // 2
        center_col = num_cols // 2

        i, j = np.ogrid[:num_rows, :num_cols]
        filter_array = np.exp(-((i - center_row) ** 2 + (j - center_col) ** 2) / (2 * sigma ** 2)) 
        return filter_array