import numpy as np
import cv2

def get_limits(color):   
    # color is a list of 3 elements [B,G,R], for example [255,0,0] for blue

    # Convert the BGR color to a numpy array
    c = np.uint8([[color]])

    # Convert the BGR color to HSV color space
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Extract the hue value from the HSV color
    h = hsvC[0][0][0]

    # Special case for red color due to hue wrapping around at 0 and 180 degrees
    if h <= 10 or h >= 170:
        # Define the first range for red
        lower_limit1 = np.array([0, 100, 100], dtype="uint8")
        upper_limit1 = np.array([h + 10, 255, 255], dtype="uint8")

        # Define the second range for red
        lower_limit2 = np.array([h - 10, 100, 100], dtype="uint8")
        upper_limit2 = np.array([180, 255, 255], dtype="uint8")
        
        # Return both ranges as tuples
        return (lower_limit1, upper_limit1), (lower_limit2, upper_limit2)
    else:
        # For other colors, define a single range around the hue value
        lower_limit = np.array([h - 10, 100, 50], dtype="uint8")
        upper_limit = np.array([h + 10, 255, 255], dtype="uint8")

        # Fine-tuning for specific colors
        if h in range(50, 70):  # Green
            lower_limit = np.array([h - 10, 50, 50], dtype="uint8")
            upper_limit = np.array([h + 10, 255, 255], dtype="uint8")
        elif h in range(140, 170):  # Pink
            lower_limit = np.array([h - 10, 100, 150], dtype="uint8")
            upper_limit = np.array([h + 10, 255, 255], dtype="uint8")
        elif h in range(100, 140):  # Blue
            lower_limit = np.array([h - 10, 100, 100], dtype="uint8")
            upper_limit = np.array([h + 10, 255, 255], dtype="uint8")

        # Return the single range as a tuple
        return lower_limit, upper_limit
