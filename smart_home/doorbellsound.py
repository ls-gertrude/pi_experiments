from gpiozero import LED, Button, Buzzer
from time import sleep
from signal import pause

led = LED(18)
button = Button(27)
buzz = Buzzer(17)

def turn_all_off(duration):
	for i in range(duration):
		led.on()
		buzz.on()
		sleep(0.1)
		led.off()
		buzz.off()
		sleep(0.1)

def alarm():
	print("alarm triggered!")
	turn_all_off(10)

button.when_pressed = alarm

pause()
