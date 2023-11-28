import Image_Filterer

class Image_Hybridizer:

    def __init__(self):
        filterer = Image_Filterer()

    def hybridize_images(self, near_image, far_image, sigma1, sigma2):
        highPassed = filterer.apply_filter(near_image, 'high_pass', sigma1)
        lowPassed = filterer.apply_filter(far_image, 'low_pass', sigma2)
        return highPassed + lowPassed