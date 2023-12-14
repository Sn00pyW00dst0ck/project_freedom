import os
import pygame
import numpy as np
from scipy.fft import fft, ifft
from scipy.io.wavfile import read, write
from scipy.signal import resample, convolve

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

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
        try:
            print(file_path)
            self.sample_rate, self.audio_data = read(file_path)
        except Exception as e:
            print(f"Error loading audio from {file_path}: {e}")
    
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

    def play_data(self):
        """
        Plays the loaded audio data using pygame and a temporary file.
        """
        self.save_to_file("temp-playing.wav")
        pygame.mixer.init()
        pygame.mixer.music.load("temp-playing.wav")
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()
        os.remove("temp-playing.wav")

    def plot_waveform(self):
        """
        Plot the waveform for the loaded audio data.
        """
        time = np.arange(0, len(self.audio_data)) / self.sample_rate
        
        plt.figure(figsize=(10, 4))
        plt.plot(time, self.audio_data, lw=0.5, color='blue')
        plt.title('Audio Waveform')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.show()
    
    def plot_frequencies(self):
        """
        Plot the frequency data for the loaded audio data.
        """
        frequencies = np.fft.fftfreq(len(self.audio_data), 1/self.sample_rate)
        magnitude_spectrum = np.abs(np.fft.fft(self.audio_data))

        plt.figure(figsize=(10, 4))
        plt.plot(frequencies, magnitude_spectrum, lw=0.5, color='blue')
        plt.title('Fourier Transform of Audio')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.show()

    def save_waveform_to_file(self, file_path):
        """
        Save a plot of the frequencies of the loaded audio data
        to a file without showing the interactive plot.

        Args:
            file_path (string):
                The file to save the plot to.
        """
        time = np.arange(0, len(self.audio_data)) / self.sample_rate
        
        plt.figure(figsize=(10, 4))
        plt.plot(time, self.audio_data, lw=0.5, color='blue')
        plt.title('Audio Waveform')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.savefig(file_path)

    def save_frequencies_to_file(self, file_path):
        """
        Save a plot of the frequencies of the loaded audio data
        to a file without showing the interactive plot.

        Args:
            file_path (string):
                The file to save the plot to.
        """
        frequencies = np.fft.fftfreq(len(self.audio_data), 1/self.sample_rate)
        magnitude_spectrum = np.abs(np.fft.fft(self.audio_data))

        plt.figure(figsize=(10, 4))
        plt.plot(frequencies, magnitude_spectrum, lw=0.5, color='blue')
        plt.title('Fourier Transform of Audio')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.savefig(file_path)

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
            padding = np.zeros((padding_length, self.audio_data.shape[1]))
            self.audio_data = np.concatenate([self.audio_data, padding])
        else:
            self.audio_data = self.audio_data[:target_length]
    
    def low_pass_filter(self, cutoff_frequency):
        """
        Apply a low pass filter to the loaded audio
        effectively isolating the low frequencies only.

        Args:
            cutoff_frequency (int): 
                The frequency at which to apply the filter.
        """
        if self.audio_data.ndim == 1:
            fft_audio = fft(self.audio_data)
            # Get the frequencies corresponding to each point in the FFT
            frequencies = np.fft.fftfreq(len(fft_audio), d=1.0/self.sample_rate)
            # Create a mask for frequencies above the cutoff
            filter_mask = np.abs(frequencies) <= cutoff_frequency
            # Apply the mask to the FFT
            filtered_fft = fft_audio * filter_mask
            self.audio_data = ifft(filtered_fft).real
            return
        
        for channel in range(self.audio_data.shape[1]):
            # Apply FFT to the audio signal
            fft_audio = fft(self.audio_data[:, channel])
            # Get the frequencies corresponding to each point in the FFT
            frequencies = np.fft.fftfreq(len(fft_audio), d=1.0/self.sample_rate)
            # Create a mask for frequencies above the cutoff
            filter_mask = np.abs(frequencies) <= cutoff_frequency
            # Apply the mask to the FFT
            filtered_fft = fft_audio * filter_mask
            # Apply Inverse FFT to obtain the filtered audio signal
            self.audio_data[:, channel] = ifft(filtered_fft).real

    def high_pass_filter(self, cutoff_frequency):
        """
        Apply a high pass filter to the loaded audio
        effectively isolating the high frequencies only.

        Args:
            cutoff_frequency (int): 
                The frequency at which to apply the filter.
        """
        if self.audio_data.ndim == 1:
            fft_audio = fft(self.audio_data)
            # Get the frequencies corresponding to each point in the FFT
            frequencies = np.fft.fftfreq(len(fft_audio), d=1.0/self.sample_rate)
            # Create a mask for frequencies above the cutoff
            filter_mask = np.abs(frequencies) >= cutoff_frequency
            # Apply the mask to the FFT
            filtered_fft = fft_audio * filter_mask
            self.audio_data = ifft(filtered_fft).real
            return
        
        for channel in range(self.audio_data.shape[1]):
            # Apply FFT to the audio signal
            fft_audio = fft(self.audio_data[:, channel])

            # Get the frequencies corresponding to each point in the FFT
            frequencies = np.fft.fftfreq(len(fft_audio), d=1.0/self.sample_rate)

            # Create a mask for frequencies above the cutoff
            filter_mask = np.abs(frequencies) >= cutoff_frequency

            # Apply the mask to the FFT
            filtered_fft = fft_audio * filter_mask

            # Apply Inverse FFT to obtain the filtered audio signal
            self.audio_data[:, channel] = ifft(filtered_fft).real

    def normalize_audio(self):
        """
        Normalize the loaded audio.
        Typically apply this operation last.
        """
        self.audio_data = np.array((np.abs(self.audio_data) / np.max(np.abs(self.audio_data))) * 32767, np.int16)

    def convolve(self, other):
        """
        Performs a convolutions between the data loaded in this 
        audio processor and the 'other' audio processor. The 
        result is stored in the calling processor.

        Note: if the sample_rates of the two processors are 
        mismatched, the sample_rate of the calling processor is 
        utilized.

        Note: This function automatically normalizes its result.

        Args:
            other (Audio_Processor):
                The other processor, with loaded data to use.
        """
        audio_data = self.audio_data.astype(np.float64)
        other_audio_data = resample(other.audio_data, int(len(other.audio_data) * self.sample_rate / other.sample_rate))
        other_audio_data = other_audio_data.astype(np.float64)

        audio_data /= np.max(np.abs(audio_data))
        other_audio_data /= np.max(np.abs(other_audio_data))
        
        convolution_result = convolve(audio_data, other_audio_data, mode='full')
        convolution_result /= np.max(np.abs(convolution_result))
        self.audio_data = (convolution_result.real * 32767).astype(np.int16)

