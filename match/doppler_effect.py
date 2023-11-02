import numpy as np

from scipy.io import wavfile


# Function to calculate the dB level from an audio file
def calculate_dB_level(file):

    global dB_level
    global dB_level_2

    if isinstance(file, str):                          # If it is a file path
        sample_rate, audio_data = wavfile.read(file)
    else:                                              # Assuming it's a numpy array
        audio_data = file

    # Check if the there is not an initial dB level
    if dB_level == float('-inf'):

        # If so, then set it
        if np.max(np.abs(audio_data)) > 0:
            dB_level = 20 * np.log10(np.max(np.abs(audio_data)))
            return dB_level, ''
        else:
            dB_level = float('-inf')

    # Otherwise, start comparisons
    else:

        # If so, then set it and compare only when there is a sound present
        if np.max(np.abs(audio_data)) > 0:
            dB_level_2 = 20 * np.log10(np.max(np.abs(audio_data)))
            compare_dB_levels(dB_level_2)
            dB_level = dB_level_2
            return dB_level, position_to_sound
        else:
            dB_level = float('-inf')


def compare_dB_levels(current_dB):

    global position_to_sound

    position_to_sound = 'Closer to the sound' if current_dB > dB_level else 'Further from the sound'


dB_level = float('-inf')
dB_level_2 = float('-inf')
position_to_sound = ''
