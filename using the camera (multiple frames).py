import cv2
import numpy as np

cap = cv2.VideoCapture(0)	#used to create instance of webcam

while True:
	ret, frame = cap.read()			#the read() stores two values : a boolean and the webcam frame
	height = int(cap.get(4))		# cap.get(4) grabs the cam height
	width = int(cap.get(3))			# cap.get(3) grabs the cam width   check docs for more arguments of cap.get()

	image = np.zeros(frame.shape, np.uint8)		#create an empty array of zeros
	small_frames = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  #create smaller frames of 1/4 the size of original
	image[:height//2, :width//2] = small_frames   #place frames acc. to array slicing methods
	image[height//2:, :width//2] = small_frames
	image[:height//2, width//2:] = small_frames
	image[height//2:, width//2:] = small_frames
	cv2.imshow('MEEEE', image)		# show the frame
	if cv2.waitKey(1) == ord('q'):  # wait every 1ms for the key 'q' to be pressed then quit
		break

cap.release()                       # release webcam 
cv2.destroyAllWindows()
