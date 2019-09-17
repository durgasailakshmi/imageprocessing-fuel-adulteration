import os
import cv2
import numpy as np

def retNum(file):
	return str(file.split("m")[0])

files = os.listdir("Average")
files.sort(key = retNum)
image1 = cv2.imread(os.path.join("Average", files[0]), 0)
image1 = cv2.equalizeHist(image1)

for i in range(1, len(files)):
	writer = open("Diff/"+files[i].split(".")[0]+".txt", "w")
	
	image2 = cv2.imread(os.path.join("Average", files[i]), 0)
	
	image2 = cv2.equalizeHist(image2)

	diff = cv2.subtract(image2,image1)
	cv2.imwrite("Diff/" + files[0] + " vs " + files[i] + ".png", np.hstack([image1,image2,diff]))
	
	for row in diff:
		writer.write(str(row))
		writer.write("\n")
	writer.close()

