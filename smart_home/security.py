import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# Setup pin 4 is button, 27 is buzzer, 17 button.
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup([17,27], GPIO.OUT)

try:
	while True:
		state =  GPIO.input(4)
		GPIO.output([17, 27], state)
		if state:
			 print("ALARM!")
		time.sleep(0.1)
except:
	GPIO.cleanup()

