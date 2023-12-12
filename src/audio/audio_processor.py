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

    self.audio_data = None
    self.sample_rate = None

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
    


    def filter_audio(self, low_cutoff, high_cutoff):
        # Apply FFT!
        frequency_domain = fft(self.audio_data)

        # Filter out selected frequencies!
        frequencies = np.fft.fftfreq(len(frequency_domain), d=1.0/self.sample_rate)
        low_mask = np.abs(frequencies) >= low_cutoff
        high_mask = np.abs(frequencies) <= high_cutoff
        mask = np.logical_and(low_mask, high_mask)
        frequency_domain = frequency_domain * mask

        # Undo FFT!
        self.audio_data = ifft(frequency_domain).real

    def normalize_audio(self):
        self.audio_data = np.array((np.abs(self.audio_data) / np.max(np.abs(self.audio_data))) * 32767, np.int16)

    def boost_volume(self, boost):
        self.audio_data = (self.audio_data.astype(np.float32) * boost).astype(np.int16)
        