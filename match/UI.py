import tkinter as tk
from tkinter import font
from threading import Thread
import time

import numpy as np

from match import record_audio, match_recording, \
    recording_duration, recording_file_path

from doppler_effect import dB_level, dB_level_2, \
    calculate_dB_level, position_to_sound


# Define a Thread class to handle audio processing in the background
class AudioProcessingThread(Thread):
    def __init__(self, update_ui_callback):
        Thread.__init__(self)
        self.update_ui_callback = update_ui_callback  # Function to call for updating the UI
        self.running = False  # Variable to control the running state of the thread

    def run(self):
        while True:  # Infinite loop to keep the thread running
            if self.running:
                # If the thread is in the running state, record audio and find the most similar file
                record_audio(recording_file_path, recording_duration)
                most_similar_file = match_recording(recording_file_path)
                self.update_ui_callback(most_similar_file)  # Update the UI with the result
                time.sleep(0.5)  # Wait a half a second before the next iteration
            else:
                time.sleep(0.1)  # Short sleep to prevent high CPU usage when not recording

    def start_recording(self):
        self.running = True  # Start the audio processing

    def stop_recording(self):
        self.running = False  # Stop the audio processing


# Function to update the UI with the most similar file and dB level (if enabled)
def update_ui(most_similar_file):

    # Update the UI to show most similar file
    result_label.config(text=most_similar_file + f' is being heard')  # Update the label with the result

    if show_dB.get():
        # Show the dB level on the UI
        calculate_dB_level(recording_file_path)  # Calculate the dB level
        dB_label.config(text=f'dB Level: {dB_level:.2f} dB')  # Update the dB level label

        # Make the UI display whether the sound is closer or further
        if dB_level_2 is not None and dB_level != -np.inf:
            dB_comparison.config(text=f'You are: ' + position_to_sound)  # Update the dB level label

    else:
        dB_label.config(text='')  # Clear the dB level label if disabled
        dB_comparison.config(text='')  # Clear the label if disabled


# Function to handle button press events
def on_circle_press(event):
    global running
    if not running:
        # If not currently recording, start recording and update the UI
        circle.itemconfig(button_circle, fill="green")
        circle.itemconfig(button_text, text="Recording", fill="white")
        audio_thread.start_recording()
        running = True
    else:
        # If currently recording, stop recording and update the UI
        circle.itemconfig(button_circle, fill="red")
        circle.itemconfig(button_text, text="Record", fill="black")
        audio_thread.stop_recording()
        running = False


# Create the main window
root = tk.Tk()
root.title("Sound Identification")
root.geometry("1000x600")

# Define various fonts for use in the UI
large_font = font.Font(size=15)
very_large_font = font.Font(size=20)
title_font = font.Font(size=24, weight='bold')

# Create a frame to hold the UI elements
frame = tk.Frame(root, padx=40, pady=40)
frame.pack(padx=20, pady=20)

# Create and pack the title label
title_label = tk.Label(frame, text="Sound Identification", font=title_font)
title_label.pack(pady=15)

# Create and pack the canvas for the recording button
circle = tk.Canvas(frame, width=100, height=100, bg='white', highlightthickness=0)
circle.pack(pady=30)

# Draw a red circle and text "Record" on the canvas
button_circle = circle.create_oval(10, 10, 90, 90, fill="red")
button_text = circle.create_text(50, 50, text="Record", font=("Arial", 12), fill="black")
circle.tag_bind(button_circle, '<Button-1>', on_circle_press)  # Bind button press event to the circle
circle.tag_bind(button_text, '<Button-1>', on_circle_press)  # Bind button press event to the text

# Create and pack the label for displaying the most similar file
result_label = tk.Label(frame, text="", font=very_large_font)
result_label.pack(pady=30)

# Create and pack the label for displaying the dB level
dB_label = tk.Label(frame, text="dB Level: ", font=large_font)
dB_label.pack(pady=10)

# Create and pack the label for displaying the closeness of a sound
dB_comparison = tk.Label(frame, text="", font=large_font)
dB_comparison.pack(pady=10)

# Create and place the settings button
settings_button = tk.Menubutton(root, text="☰", font=("Arial", 15), relief=tk.FLAT)
settings_button.place(x=10, y=10)

# Create the settings menu with a checkbutton to show/hide dB level
settings_menu = tk.Menu(settings_button, tearoff=0)
settings_button["menu"] = settings_menu
show_dB = tk.BooleanVar()
show_dB.set(True)  # dB level is shown by default
settings_menu.add_checkbutton(label="Show dB Level", onvalue=True, offvalue=False, variable=show_dB)

# Initialize the running state and start the audio processing thread
running = False
audio_thread = AudioProcessingThread(update_ui)
audio_thread.start()

# Start the main loop of the application
root.mainloop()
