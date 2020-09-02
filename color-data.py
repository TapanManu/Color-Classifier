import pandas as pd
import numpy as np
import cv2
import csv

count=0

# color dataset creation

def colors(B,G,R):
	cv2.namedWindow('mouseRGB')
	#cv2.setMouseCallback('mouseRGB',RGBCapture)
	capture = cv2.VideoCapture(0)
	c=""
	
	while(True):

	    ret, frame = capture.read()
   
	    cv2.circle(frame, (100,100),30, (B,G,R), 2)

	    cv2.imshow('mouseRGB', frame)

	    if cv2.waitKey(1) == ord('t'):
	    	c = input("enter input color:")
	    	break


	capture.release()
	cv2.destroyAllWindows()
	return str(c)

df = pd.read_csv('colours_rgb_shades.csv')
print(df.isnull().sum())
empty = np.where(pd.isnull(df))[0]		#getting row indices of empty colors
rows=[[]]
for i in empty:
	if(count==0):
		t='w'
	else:
		t='a'
	print("get the color in each loop")
	R = int(df['R'][i:i+1])
	G = int(df['G'][i:i+1])
	B = int(df['B'][i:i+1])
	bgr = colors(B,G,R)
	df['matching color'][i]=bgr
	nested = [df['Color Name'][i],R,G,B,df['matching color'][i]]
	rows.append(nested)
	#color_rgb_shades.csv is a temporary file to store the data and later written to colours_rgb_shades.csv
	#remove/delete color_rgb_shades.csv
	with open('colour_rgb_shades.csv',t) as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(nested)
	count+=1




