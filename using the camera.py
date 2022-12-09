import cv2

cap = cv2.VideoCapture(0)	#used to create instance of webcam

while True:
	ret, frame = cap.read()	
	width = int(cap.get(3))  		#get the width 
	height = int(cap.get(4))		#get the height

	cv2.imshow("Using the camera", frame)
 	
	if cv2.waitKey(1) == ord('q'):  # wait for the key 'q' to be pressed then quit
		break

cap.release()                       # cleanup
cv2.destroyAllWindows()
