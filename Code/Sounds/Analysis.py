import os
import sqlite3
import numpy as np
import librosa

# ---------------- Sound Feature Extraction ----------------

def extract_features(file_name):
    y, sr = librosa.load(file_name)
    D = librosa.stft(y)
    spect_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    
    frequency_index = np.argmax(spect_db, axis=0)
    frequencies = librosa.fft_frequencies(sr=sr)
    dominant_frequencies = frequencies[frequency_index]
    dominant_amplitudes = np.max(spect_db, axis=0)

    return dominant_frequencies, dominant_amplitudes

# ---------------- Database Functions ----------------

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    conn.close()

def insert_sound_data(db_name, file_name, frequencies, amplitudes):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    freq_str = ','.join(map(str, frequencies))
    amp_str = ','.join(map(str, amplitudes))

    cursor.execute( (file_name, freq_str, amp_str))
    
    conn.commit()
    conn.close()

# ---------------- Main Run ----------------

if __name__ == "__main__":
    db_name = 'sounds.db'
    create_database(db_name)

    sound_files = [
        "car-horns.wav", 
        "dog-barking.wav", 
        "doorbell.wav", 
        "kitchen-sink.wav", 
        "knock_wood_10_times.wav", 
        "male-shouting-yelling-hey.wav", 
        "smoke-detector-alarm.wav", 
        "train-horn-and-bell.wav"
    ]

    for sound_file in sound_files:
        frequencies, amplitudes = extract_features(sound_file)
        insert_sound_data(db_name, sound_file, frequencies, amplitudes)
        print(f"Data for {sound_file} has been successfully stored into {db_name}.")
