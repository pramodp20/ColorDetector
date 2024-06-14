import cv2
from util import get_limits
from PIL import Image

# Define BGR color values
colors = [
    [255, 0, 0],     # Blue 0
    [0, 255, 0],     # Green 1
    [0, 0, 255],    # Red 2
    [0, 255, 255],  # Yellow 3
    [255, 0, 255],  # Magenta 4
    [255, 255, 0],  # Cyan 5
    [255, 255, 255],  # White 6
    [0, 0, 0]  # Black 7    
]


# Open a connection to the default camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Capture a frame from the camera

    if not ret:  # Break the loop if frame is not captured
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame to HSV color space

    limits = get_limits(colors[2])  # Get the HSV limits for the red color

    if isinstance(limits, tuple) and len(limits) == 2 and isinstance(limits[0], tuple):
        # If there are two sets of limits (for red)
        lower_limit1, upper_limit1 = limits[0]
        lower_limit2, upper_limit2 = limits[1]

        # Create masks for both ranges and combine them
        mask1 = cv2.inRange(hsv_frame, lower_limit1, upper_limit1)
        mask2 = cv2.inRange(hsv_frame, lower_limit2, upper_limit2)
        
        mask = cv2.bitwise_or(mask1, mask2)
    else:
        # For other colors with a single range
        lower_limit, upper_limit = limits
        mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)  # Convert the mask to a PIL image

    bbox = mask_.getbbox()  # Get the bounding box of the masked area

    if bbox:  # If a bounding box is found, draw a rectangle around it
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("mask", mask)  # Display the mask
    cv2.imshow("actual", frame)  # Display the frame with the rectangle

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop if 'q' is pressed
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows
