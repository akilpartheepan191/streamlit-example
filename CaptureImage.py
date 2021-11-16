import cv2

import time

def captureImageFunction():
	
		# Opens the inbuilt camera of laptop to capture video.
		cap = cv2.VideoCapture(0)
		i = 0
		time.sleep(5)
		ret, frame = cap.read()
		# Save Frame by Frame into disk using imwrite method
		cv2.imwrite('CapturedFrame'+str(i)+'.jpg', frame)
		print("captured")
		cap.release()
		cv2.destroyAllWindows()

captureImageFunction()
