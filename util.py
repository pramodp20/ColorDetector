import numpy as np
import cv2

def get_limits(color):   # color ia a list of 3 elements [B,G,R] exaple [255,0,0] for blue

    c = np.uint8([[color]]) # here insert the bgr values which you want to convert to hsv

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) # convert it to hsv exaple [120,255,255] for blue

    lower_limit = hsvC[0][0][0] - 100, 100, 100 # lower limit of the color range exaple [110,100,100] for blue
    upper_limit = hsvC[0][0][0] + 100, 255, 255 # upper limit of the color range exaple [130,255,255] for blue

    lower_limit = np.array(lower_limit, dtype="uint8") # convert the list to numpy array
    upper_limit = np.array(upper_limit, dtype="uint8") # convert the list to numpy array

    return lower_limit,upper_limit