import tkinter as tk
from tkinter import font
from match import record_audio, match_recording, recording_duration, recording_file_path, folder_path

def update_result():
    record_audio(recording_file_path, recording_duration)
    most_similar_file = match_recording(recording_file_path, folder_path)
    # Display the result on the GUI
    result_label.config(text='Most similar wav: ' + most_similar_file)
    
    if running:  # Only reschedule if still running
        # Schedule next update after 3 seconds (3000 milliseconds)
        global after_id
        after_id = root.after(3000, update_result)

def on_circle_press(event):
    global running
    if not running:
        circle.itemconfig(button_circle, fill="green")
        running = True
        root.after(0, update_result)  # Start the process after changing the button color
    else:
        circle.itemconfig(button_circle, fill="red")
        running = False
        if after_id:
            root.after_cancel(after_id)  # Use the after_id to cancel the scheduled function

root = tk.Tk()
root.title("Sound Identification")
root.geometry("1000x600")

# Define fonts
large_font = font.Font(size=15)
very_large_font = font.Font(size=20)
title_font = font.Font(size=24, weight='bold')

frame = tk.Frame(root, padx=40, pady=40)
frame.pack(padx=20, pady=20)

title_label = tk.Label(frame, text="Sound Identification", font=title_font)
title_label.pack(pady=15)

# Create a canvas for the circle button
circle = tk.Canvas(frame, width=100, height=100, bg='white', highlightthickness=0)
circle.pack(pady=30)

# Draw a circle on the canvas and set its initial color to red
button_circle = circle.create_oval(10, 10, 90, 90, fill="red")

# Bind the circle to the function on_circle_press
circle.tag_bind(button_circle, '<Button-1>', on_circle_press)  

result_label = tk.Label(frame, text="", font=very_large_font)
result_label.pack(pady=30)

running = False  # Variable to keep track of the running state
after_id = None  # Variable to store the ID returned by root.after() 
root.mainloop()




