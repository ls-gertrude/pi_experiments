import cv2
camera = cv2.VideoCapture(0)

while True:
	ret,frame = camera.read()
	if not ret:
		print("could not return from cam")
		break
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_red = (0,100,100)
	higher_red = (10,255,255)
	mask = cv2.inRange(hsv, lower_red, higher_red)

	cv2.imshow("Robot camera", frame)
	cv2.imshow("Red Detectection", mask)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
camera.release()
cv2.destroyAllWindows()
