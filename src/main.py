"""Main Executable Program File"""

import numpy as np
import imageio.v3 as iio

from images.image_processor import Image_Processor
from audio.audio_processor import Audio_Processor

AUDIO_FILE_BASE = "./assets/audio/"
IMAGE_FILE_BASE = "./assets/images/"
VIDEO_FILE_BASE = "./assets/videos/"

audio_file_processor = Audio_Processor()
image_file_processor = Image_Processor()

if __name__ == "__main__":
    # Grayscale works.
    # RGB kinda works.
    # Audio mods are working. 
    # TODO: Let's try for Video.
    # TODO: Let's write a really good explanation document.

    image_file_processor.load_from_file(IMAGE_FILE_BASE + "rgb_einstein.png")
    second_processor = Image_Processor()
    second_processor.load_from_file(IMAGE_FILE_BASE + "rgb_monroe.png")

    image_file_processor.custom_hybridization(second_processor, 23, 14)
    image_file_processor.save_to_file("combined_updated.png")
    image_file_processor.display_image()

    print("Done modifying image!")

    # Replace below with a loop for processing images & data

    processor1 = Audio_Processor()
    processor1.load_from_file(AUDIO_FILE_BASE + "dog_bark_dry.wav")
    processor2 = Audio_Processor()
    processor2.load_from_file(AUDIO_FILE_BASE + "concert_hall_ir.wav")

    processor1.convolve(processor2)
    processor1.save_to_file("cross_synth.wav")
    processor1.play_data()
    print(processor1.audio_data)

    print("Done modifying audio!")


