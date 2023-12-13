"""Main Executable Program File"""

import numpy as np
import imageio.v3 as iio

from images.image_hybridizer import Image_Hybridizer
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
    # TODO: Let's try for Video.
    # TODO: Let's write a really good explanation document.

    image_file_processor.load_from_file(IMAGE_FILE_BASE + "rgb_einstein.png")
    second_processor = Image_Processor()
    second_processor.load_from_file(IMAGE_FILE_BASE + "rgb_monroe.png")

    image_file_processor.custom_hybridization(second_processor, 23, 14)
    image_file_processor.save_to_file("combined_updated.png")
    image_file_processor.display_image()

    #Ethan_Hunt = iio.imread(IMAGE_FILE_BASE + "rgb_monroe.png")
    #James_Bond = iio.imread(IMAGE_FILE_BASE + "rgb_einstein.png")

    ## Grab the channels of RGB Image
    #Ethan_R = Ethan_Hunt[:, :, 0]
    #Ethan_G = Ethan_Hunt[:, :, 1]
    #Ethan_B = Ethan_Hunt[:, :, 2]

    #James_R = James_Bond[:, :, 0]
    #James_G = James_Bond[:, :, 1]
    #James_B = James_Bond[:, :, 2]

    #hybridizer = Image_Hybridizer()

    #hybrid_image = hybridizer.hybridize_images(James_Bond[:,:,0], Ethan_Hunt[:,:,0], 23, 14)
    ## hybrid_g = hybridizer.hybridize_images(James_G, Ethan_G, 23, 14)
    ## hybrid_b = hybridizer.hybridize_images(James_B, Ethan_B, 23, 14)
    ## hybrid_image = np.dstack((hybrid_r, hybrid_g, hybrid_b))

    #iio.imwrite("combined.png", hybrid_image.astype(np.uint8))

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

    # processor1.low_pass_filter(750)
    # processor2.high_pass_filter(750)

    # processor1.normalize_audio()
    # processor1.save_to_file("low_pass_oddity.wav")
    # processor2.normalize_audio()
    # processor2.save_to_file("high_pass_lewis.wav")

    # hybridizer = Audio_Hybridizer()
    # merged = hybridizer.hybridize_audio(processor1.audio_data, processor2.audio_data, 0.5)

    # processor3 = Audio_Processor()
    # processor3.load_from_data(merged, processor1.sample_rate)
    # processor3.normalize_audio()
    # processor3.save_to_file("hybrid.wav")

    print("Done modifying audio!")


