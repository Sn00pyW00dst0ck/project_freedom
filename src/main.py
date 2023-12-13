"""Main Executable Program File"""

from images.image_processor import Image_Processor
from audio.audio_processor import Audio_Processor

AUDIO_FILE_BASE = "./assets/audio/"
IMAGE_FILE_BASE = "./assets/images/"
VIDEO_FILE_BASE = "./assets/videos/"

audio_file_processor = Audio_Processor()
image_file_processor = Image_Processor()

def get_positive_integer_input(prompt):
    """
    Repeatedly prompts the user until they provide 
    a valid positive integer input.

    Args:
        prompt (str): A string to prompt the user with.
    Returns: 
        int: A positive integer > 0 entered by the user.
    """
    while True:
        try:
            value = int(input(prompt)) # Will raise a ValueError if input is not an int
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_string_input(prompt):
    """
    Repeatedly prompt the user for a string input

    Args:
        prompt (string):
            The prompt to dispaly to the user.
        
    Returns:
        string:
            The value the user entered
    """
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Invalid input.")

def get_valid_string_input(prompt, choices):
    """
    Repeatedly prompt the user for a valid string input

    Args:
        prompt (string):
            The prompt to dispaly to the user.
        
        choices (list<string>):
            The valid choices for responses.
    Returns:
        string:
            The value the user entered
    """
    while True:
        try:
            value = input(prompt) # Will raise a ValueError if input is not an int
            if value not in choices:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    print("Welcome to Project Freedom!")

    # Start main menu loop
    while True:
        choice = get_valid_string_input(
            "Would you like to work with audio or images?\n" + 
            "Enter 'audio' or 'images', or 'q' to exit: ",
            ["audio", "images", "q"]
        )
    
        if choice == "q":
            print("Thank you for using Project Freedom! Goodbye!")
            exit(0) 

        if choice == "audio":
            # Load the initial file
            choice = get_string_input(
                "What audio file would you like to use?\n" +
                "Enter audio file name: "
            )
            print("Loading file: " + AUDIO_FILE_BASE + choice)
            audio_file_processor.load_from_file(AUDIO_FILE_BASE + choice)
            print("File successfully loaded.")

            # Start audio manipulation menu loop
            while True:
                choice = get_valid_string_input(
                    "What would you like to do?\n\n" +
                    "1. Play current audio\n" + 
                    "2. View current audio waveform\n" + 
                    "3. Save current audio waveform\n" +
                    "4. View current audio fourier transform\n" + 
                    "5. Save current audio fourier transform\n" +
                    "6. Apply low pass filter\n" +
                    "7. Apply high pass filter\n" +
                    "8. Convolve with another audio\n" +
                    "9. Load a different audio\n" +
                    "10. Return to main menu\n\n" +
                    "Enter your choice: ",
                    ["1","2","3","4","5","6","7","8","9","10"]
                )

                match choice:
                    case "1":
                        audio_file_processor.play_data()
                    case "2":
                        audio_file_processor.plot_waveform()
                    case "3":
                        file_location = get_string_input(
                            "Where would you like to save the waveform plot?\n" +
                            "Enter file name: "
                        )
                        audio_file_processor.save_waveform_to_file(file_location)
                    case "4":
                        audio_file_processor.plot_frequencies()
                    case "5":
                        file_location = get_string_input(
                            "Where would you like to save the fourier transform plot?\n" +
                            "Enter file name: "
                        )
                        audio_file_processor.save_frequencies_to_file(file_location)
                    case "6":
                        cutoff = get_positive_integer_input(
                            "What is the highest frequency to keep?\n" +
                            "Enter frequency: "
                        )
                        audio_file_processor.low_pass_filter(cutoff)
                    case "7":
                        cutoff = get_positive_integer_input(
                            "What is the lowest frequency to keep?\n" +
                            "Enter frequency: "
                        )
                        audio_file_processor.high_pass_filter(cutoff)
                    case "8":
                        choice = get_string_input(
                            "What audio file would you like to convolve with?\n" +
                            "Enter audio file name: "
                        )
                        temp_audio_processor = Audio_Processor()
                        temp_audio_processor.load_from_file(AUDIO_FILE_BASE + choice)
                        print("File successfully loaded, convolving audio...") 
                        audio_file_processor.convolve(temp_audio_processor)
                        print("Audio succesfully convolved.")
                    case "9":
                        choice = get_string_input(
                            "What audio file would you like to use?\n" +
                            "Enter audio file name: "
                        )
                        print("Loading file: " + AUDIO_FILE_BASE + choice)
                        audio_file_processor.load_from_file(AUDIO_FILE_BASE + choice)
                        print("File successfully loaded.")
                    case "10":
                        break
                    case _:
                        print("Shouldn't be here!")
                        


        if choice == "images":
            # Load the initial file
            choice = get_string_input(
                "What image file would you like to use?\n" +
                "Enter image file name: "
            )
            print("Loading file: " + IMAGE_FILE_BASE + choice)
            image_file_processor.load_from_file(IMAGE_FILE_BASE + choice)
            print("File successfully loaded.")

            # Start image manipulation menu loop (TODO: add option to apply filter)
            while True:
                choice = get_valid_string_input(
                    "What would you like to do?\n\n" +
                    "1. View current image\n" + 
                    "2. Save current image\n" + 
                    "3. View current image fourier transform\n" +
                    "4. Save current image fourier transform\n" + 
                    "5. Apply low pass filter\n" +
                    "6. Apply high pass filter\n" +
                    "7. Hybridize with another image\n" +
                    "8. Load a different image\n" +
                    "9. Return to main menu\n\n" +
                    "Enter your choice: ",
                    ["1","2","3","4","5","6","7","8","9"]
                )

                match choice:
                    case "1":
                        image_file_processor.plot_image()
                    case "2":
                        file_location = get_string_input(
                            "Where would you like to save the image?\n" +
                            "Enter file name: "
                        )
                        image_file_processor.save_to_file(file_location)
                    case "3":
                        image_file_processor.plot_fourier_transform()
                    case "4":
                        file_location = get_string_input(
                            "Where would you like to save the fourier transform?\n" +
                            "Enter file name: "
                        )
                        image_file_processor.save_to_file(file_location)
                    case "5":
                        sigma_low = get_positive_integer_input(
                            "Enter the value of sigma to use in the low pass filter.\n" + 
                            "Sigma: "
                        )
                        image_file_processor.image_data = image_file_processor.apply_filter("low_pass", sigma_low)
                    case "6":
                        sigma_high = get_positive_integer_input(
                            "Enter the value of sigma to use in the high pass filter.\n" + 
                            "Sigma: "
                        )
                        image_file_processor.image_data = image_file_processor.apply_filter("high_pass", sigma_high)
                    case "7":
                        file_location = get_string_input(
                            "What image would you like to hybridize with?\n" +
                            "Enter file name: "
                        )
                        print("Loading file: " + IMAGE_FILE_BASE + file_location)
                        temp_image_processor = Image_Processor()
                        temp_image_processor.load_from_file(IMAGE_FILE_BASE + file_location)
                        print("File successfully loaded, hybridizing images...")
                        sigma_low = get_positive_integer_input(
                            "Enter the value of sigma to use in the low pass filter.\n" + 
                            "Sigma: "
                        )
                        sigma_high = get_positive_integer_input(
                            "Enter the value of sigma to use in the high pass filter.\n" + 
                            "Sigma: "
                        )
                        image_file_processor.custom_hybridization(temp_image_processor, sigma_high, sigma_low) # 23, 14)
                        print("Hybridization complete!")
                    case "8":
                        choice = get_string_input(
                            "What image file would you like to use?\n" +
                            "Enter image file name: "
                        )
                        print("Loading file: " + IMAGE_FILE_BASE + choice)
                        image_file_processor.load_from_file(IMAGE_FILE_BASE + choice)
                        print("File successfully loaded.")
                    case "9":
                        break
                    case _:
                        print("Shouldn't be here!")



    # Grayscale works.
    # RGB kinda works.
    # Audio mods are working. 
    # TODO: Let's try for Video.
    # TODO: Let's write a really good explanation document.
    image_file_processor.load_from_file(IMAGE_FILE_BASE + "einstein.png")
    image_file_processor.plot_image()
    image_file_processor.plot_fourier_transform()
    image_file_processor.save_fourier_transform_to_file(IMAGE_FILE_BASE + "fourier.png")

    image_file_processor.load_from_file(IMAGE_FILE_BASE + "rgb_einstein.png")
    image_file_processor.plot_image()
    second_processor = Image_Processor()
    second_processor.load_from_file(IMAGE_FILE_BASE + "rgb_monroe.png")

    image_file_processor.custom_hybridization(second_processor, 23, 14)
    image_file_processor.save_to_file("combined_updated.png")
    image_file_processor.plot_image()

    print("Done modifying image!")

    # Replace below with a loop for processing images & data

    processor1 = Audio_Processor()
    processor1.load_from_file(AUDIO_FILE_BASE + "dog_bark_dry.wav")
    processor1.plot_waveform()
    processor1.plot_frequencies()
    processor2 = Audio_Processor()
    processor2.load_from_file(AUDIO_FILE_BASE + "concert_hall_ir.wav")

    processor1.convolve(processor2)
    processor1.save_to_file("cross_synth.wav")
    processor1.play_data()

    print("Done modifying audio!")


