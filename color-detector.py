import cv2
import numpy as np
import pandas as pd
import pickle

#colormap taken accordingly , do not change the values!!!
colormap = {'grey': 0, 'white': 1, 'blue': 2, 'black': 3, 'violet': 4, 'green': 5, 'pink': 6, 'magenda': 7, 
'orange': 8, 'red': 9, 'brown': 10, 'magenta': 11, 'lemon': 12, 'yellow': 13, 'purple': 14}

def color(value):
    for item in colormap.items():
        if(item[1]==value[0]):
            return item[0]
    return item[0][1]

def RGBCapture(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
        colors = frame[y,x]
        print("Red:",colorsR," Green:",colorsG," Blue:",colorsB)
        print("Coordinates of pixel: X: ",x,"Y: ",y)
        print("color is:",color(model.predict([[colorsR,colorsG,colorsB]])))

#model has some ambiguity regarding orange,brown ... rest are good in working

model = pickle.load(open('colour_model.sav','rb'))
cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',RGBCapture)


capture = cv2.VideoCapture(0)

while(True):

    ret, frame = capture.read()

    cv2.imshow('mouseRGB', frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

