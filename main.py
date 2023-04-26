import cv2 as cv
import numpy as np
from mss import mss
import pygetwindow


with mss() as sct:

    while True:    
        window_geometry = pygetwindow.getWindowGeometry('Google Chrome')

        bbox = (window_geometry[0],
                window_geometry[1],
                window_geometry[0] + window_geometry[2],
                window_geometry[1] + window_geometry[3])
        
        im = np.array(sct.grab(bbox))

        cv.imshow('Terminal imshow', im)
        cv.waitKey(1)








