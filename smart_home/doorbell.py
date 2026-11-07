from gpiozero import LED, Button, Buzzer
from signal import pause

button = Button(27)
led = LED(18)
buzz = Buzzer(17)

# code to turn it on when pressed
def turn_all():
	led.on()
	buzz.on()

#code to turn it off when pressed
def turn_off():
	led.off()
	buzz.off()

button.when_pressed = turn_all
button.when_released = turn_off

print("doorbell ringing")

pause()
