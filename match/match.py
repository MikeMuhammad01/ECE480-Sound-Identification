import math
import os

import librosa
import numpy as np
import sounddevice as sd

from dtw import dtw
from librosa.feature import mfcc
from scipy.io import wavfile
from scipy.signal import find_peaks
from scipy.fft import fft


def extract_features(file_path):

    audio, fs = librosa.load(file_path)
    fft_audio = fft(audio)
    peaks = find_peaks(fft_audio, distance=int(fs/5))

    # Computing MFCC values
#    features.append(np.max(mfcc(y=audio, sr=fs)))
#    features.append(np.min(mfcc(y=audio, sr=fs)))
    return peaks[0]


def compute_similarity(features1, features2):
    return math.dist(features1, features2)


def match_recording(recording_path):
    recording_features = extract_features(recording_path)
    max_similarity = float('inf')
    most_similar_file = None

    for file_name in os.listdir(repository_path):
        if file_name.endswith('.wav'):
            file_path = os.path.join(repository_path, file_name)
            file_features = extract_features(file_path)
            similarity = compute_similarity(recording_features, file_features)

            if similarity < max_similarity:
                max_similarity = similarity
                most_similar_file = file_name

    return most_similar_file


def record_audio(file_path, duration):
    fs = 44100  
    print("recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wavfile.write(file_path, fs, audio)


def calculate_dB_level(audio_data_or_file_path):
    if isinstance(audio_data_or_file_path, str):  # if it's a file path
        sample_rate, audio_data = wavfile.read(audio_data_or_file_path)
    else:  # assuming it's a numpy array
        audio_data = audio_data_or_file_path

    amplitude = np.max(np.abs(audio_data))
    if amplitude > 0:
        dB_level = 20 * np.log10(amplitude)
        return dB_level
    else:
        return -np.inf


recording_duration = 5
recording_file_path = 'recording.wav'
repository_path = 'Sounds/'

