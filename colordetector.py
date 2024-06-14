import cv2
import numpy as np
import tkinter as tk
from tkinter import Label

# Define primary color ranges in HSV
color_ranges = {
    "Red": ((0, 100, 100), (10, 255, 255)),
    "Green": ((60, 100, 100), (80, 255, 255)),
    "Blue": ((100, 100, 100), (130, 255, 255)),
    "White": ((0, 0, 200), (180, 20, 255)),
    "Black": ((0, 0, 0), (180, 30, 30)),
    "Yellow": ((20, 100, 100), (30, 255, 255)),
    "Pink": ((160, 100, 100), (180, 255, 255)),
    "Orange": ((10, 100, 100), (20, 255, 255))
}

def detect_color(hsv_frame):
    for color_name, (lower, upper) in color_ranges.items():
        lower_np = np.array(lower, dtype="uint8")
        upper_np = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv_frame, lower_np, upper_np)
        if np.any(mask):
            
            return color_name
    return "Unknown"

def update_color_label(color):
    color_label.config(text=color)
    root.update()

# Initialize Tkinter window
root = tk.Tk()
root.title("Detected Color")
color_label = Label(root, text="", font=("Helvetica", 24))
color_label.pack(pady=20)

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    detected_color = detect_color(hsv_frame)
    
    # Update Tkinter window with detected color
    update_color_label(detected_color)
    
    # Display the frame
    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
root.destroy()
