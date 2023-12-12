import numpy as np

class Audio_Hybridizer:
    def __init__(self):
        pass
    
    def hybridize_audio(self, audio1, audio2, hybridization_factor):
        min_length = min(len(audio1), len(audio2))

        # Apply FFT
        fft1 = np.fft.fft(audio1[:min_length]) # low
        fft2 = np.fft.fft(audio2[:min_length]) # high

        # Combine frequency components
        hybrid_fft = (hybridization_factor * fft1) + ((1 - hybridization_factor) * fft2)

        # Apply Inverse FFT
        hybrid_audio = np.fft.ifft(hybrid_fft).real

        return hybrid_audio

    def hybridize_audio_alt(self, audio1, audio2, freq):
        min_length = min(len(audio1), len(audio2))

        # Apply FFT
        fft1 = np.fft.fft(audio1[:min_length]) # low
        fft2 = np.fft.fft(audio2[:min_length]) # high

        # Combine frequency components
        low_freq_indices = np.where(np.abs(fft1) < freq)
        high_freq_indices = np.where(np.abs(fft2) >= freq)
        print(low_freq_indices)
        print(high_freq_indices)

        hybrid_fft = np.zeros_like(fft1)
        hybrid_fft[low_freq_indices] = fft1[low_freq_indices]
        hybrid_fft[high_freq_indices] = fft2[high_freq_indices]

        # Apply Inverse FFT
        hybrid_audio = np.fft.ifft(hybrid_fft).real
        return hybrid_audio
