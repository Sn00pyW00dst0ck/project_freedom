import numpy as np
from scipy.fft import fft, ifft
from scipy.io.wavfile import read, write
import sounddevice as sd

class Audio_Processor:
    """
    A class for easily working with audio.
    Provides methods for loading audio, 
    saving audio to a file, and performing
    basic operations on audio.
    """

    audio_data = None
    sample_rate = None

    def __init__(self):
        pass

    def load_from_file(self, file_path):
        """
        Loads audio to be processed from a file.

        Args:
            file_path (string):
                The path from which to load the audio data!
        """
        self.sample_rate, self.audio_data = read(file_path)
    
    def load_from_data(self, audio_data, sample_rate):
        """
        Loads audio to be processed from data.

        Args:
            audio_data (np.array):
                The audio samples to load.
            
            sample_rate (int):
                The sampling rate for the audio.
        """
        self.audio_data = audio_data
        self.sample_rate = sample_rate

    def save_to_file(self, file_path):
        """
        Saves the loaded audio to a file.

        Args:
            file_path (string):
                The path to save the audio data to!
        """
        write(file_path, self.sample_rate, self.audio_data.astype(np.int16))
    
    def pad_to_length(self, target_length):
        """
        Pads the end of the loaded audio with 
        silence to match the desired length,
        or cuts the audio file to match the 
        desired length.

        Args:
            target_length (string):
                The desired number of audio samples 
        """
        current_length = self.audio_data.shape[0]

        if current_length < target_length:
            padding_length = target_length - current_length
            padding = np.zeros(padding_length)
            self.audio_data = np.concatenate([self.audio_data, padding])
        else:
            self.audio_data = self.audio_data[:target_length]
    
    def low_pass_filter(self, cutoff_frequency):
        # Apply FFT to the audio signal
        fft_audio = fft(self.audio_data)

        # Get the frequencies corresponding to each point in the FFT
        frequencies = np.fft.fftfreq(len(fft_audio), d=1.0/self.sample_rate)

        # Create a mask for frequencies above the cutoff
        filter_mask = np.abs(frequencies) <= cutoff_frequency

        # Apply the mask to the FFT
        filtered_fft = fft_audio * filter_mask

        # Apply Inverse FFT to obtain the filtered audio signal
        self.audio_data = ifft(filtered_fft).real

    def high_pass_filter(self, cutoff_frequency):
        # Apply FFT to the audio signal
        fft_audio = fft(self.audio_data)

        # Get the frequencies corresponding to each point in the FFT
        frequencies = np.fft.fftfreq(len(fft_audio), d=1.0/self.sample_rate)

        # Create a mask for frequencies above the cutoff
        filter_mask = np.abs(frequencies) >= cutoff_frequency

        # Apply the mask to the FFT
        filtered_fft = fft_audio * filter_mask

        # Apply Inverse FFT to obtain the filtered audio signal
        self.audio_data = ifft(filtered_fft).real

    def normalize_audio(self):
        self.audio_data = np.array((np.abs(self.audio_data) / np.max(np.abs(self.audio_data))) * 32767, np.int16)

    def boost_volume(self, boost):
        self.audio_data = (self.audio_data.astype(np.float32) * boost).astype(np.int16)
        