import os, io
import warnings
import numpy as np
import sounddevice as sd
import soundfile as sf
from fastdtw import fastdtw
from scipy.io import wavfile
from python_speech_features import mfcc

warnings.filterwarnings("ignore", category=wavfile.WavFileWarning)

def extract_features(file_path):
    sample_rate, audio = wavfile.read(file_path)
    features = mfcc(audio, sample_rate, nfft=2048)
    return features

def compute_similarity(features1, features2):
    distance, _ = fastdtw(features1, features2)
    similarity = 1 / (1 + distance)
    return similarity

def match_recording(record_path, folder_path):
    recording_features = extract_features(record_path)
    max_similarity = -np.inf
    most_similar_file = None

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.wav'):
            print(file_name, end=': \t\t')
            file_path = os.path.join(folder_path, file_name)
            file_features = extract_features(file_path)
            similarity = compute_similarity(recording_features, file_features)
            print(similarity)

            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_file = file_name
    return most_similar_file

""""
def record_audio(file_path, duration):
    fs = 44100  
    print("recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wavfile.write(file_path, fs, audio)
"""
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
