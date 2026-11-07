from gpiozero import MotionSensor
import cv2
from datetime import datetime
import time

# Setup
pir = MotionSensor(23)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
	print("Camera not detected")
	exit()

print("=========")
print(" SENTINEL")
print("=========")
print("Security system armed")
print("Waiting for motion...")

try:
	while True:
		pir.wait_for_motion()
		print("\nMotion Detected")
		time.sleep(1)

		for _ in range(5):
			ret, frame = camera.read()

		if ret:
			timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
			filename = f"evidence_{timestamp}.jpg"
			cv2.imwrite(filename, frame)
			print(f" Photo saved: {filename}")
		else:
			print("Failed to capture photo")
		time.sleep(3)

		print(" Waiting for motion...")

except KeyboardInterrupt:
	print("\nSecurity system shutting down.")

finally:
	camera.release()
	cv2.destroyAllWindows()
