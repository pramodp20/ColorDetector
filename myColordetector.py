import cv2 
from util import get_limits
from PIL import Image

yellow = [0,255,255]
red = [0,0,255]
blue = [255,0,0]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(red)

    mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("mask", mask)
    cv2.imshow("actual", frame)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()