import os
import cv2
import numpy as np
import copy

folders = os.listdir()
folders.remove("Average")
folders.remove("Difference")

for folder in folders:
	#checks if folder exists
	if not os.path.isdir(folder):
		continue

	average = np.zeros([300,300,3], dtype = int)
	n = 0
	files = os.listdir(folder)	
	print("Processing " + folder)
	for file in files:
		ext = file.split(".")[1]
		#Read JPG files only
		if ext.upper() != 'JPG':
			continue
		#Read the file
		image = cv2.imread( os.path.join(folder,file))
		
		image = cv2.resize(image, (image.shape[1]//8, image.shape[0]//8)) 
		gray1 = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)
		gray = cv2.cvtColor( image, cv2.COLOR_BGR2HSV)
		circles = cv2.HoughCircles(gray1, cv2.HOUGH_GRADIENT, 1.2, 100)
		output = copy.deepcopy(image)


		if circles is not None:
			circles = np.round(circles[0, :]).astype("int")
			for (x, y, r) in circles:
				output = np.array(output[ y-r:y+r, x-r:x+r, : ])
				#Resize to standard format of 300x300
				output = cv2.resize(output, (300,300))
				average += output
				n += 1

	#Average of n images in a folder
	average = average/n
	average = np.uint8(average)
	filename = "Average/"+folder+".png"
	print(filename)
	cv2.imwrite(filename, average)


	
