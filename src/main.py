"""Main Executable Program File"""

import numpy as np
import imageio.v3 as iio

from images.image_hybridizer import Image_Hybridizer

if __name__ == "__main__":
    # Grayscale works.
    # TODO: Let's try RGB.
    # TODO: Let's try for Video.
    # TODO: Let's try for Music.
    # TODO: Let's write a really good explanation document.

    Ethan_Hunt = iio.imread("Ethan_Hunt.jpg")
    James_Bond = iio.imread("James_Bond.jpg")
    Ethan_Hunt = Ethan_Hunt[:, :, 0]
    James_Bond = James_Bond[:, :, 0]

    hybridizer = Image_Hybridizer()

    hybrid_image = hybridizer.hybridize_images(James_Bond, Ethan_Hunt, 29, 14)
    hybrid_image = np.clip(np.abs(hybrid_image), 0, 255)
    iio.imwrite("combined.png", hybrid_image.astype(np.uint8))

    print("Done!")
