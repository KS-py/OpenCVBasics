import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
	check, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	

	for (x,y,w,h) in faces:
		print(x,y,w,h)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		eye_gray = gray[y:y+w, x:x+w]
		eye_color = frame[y:y+h, x:x+h]
		eyes = eye_cascade.detectMultiScale(eye_gray, 1.3, 5)
		for (eye_x, eye_y, eye_w, eye_h) in eyes:
			cv2.rectangle(eye_color, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (0, 255, 255), 2)




	cv2.imshow("Window", frame)
	if cv2.waitKey(1) == ord('q'):
		break 

cap.release()
cv2.destroyAllWindows()
