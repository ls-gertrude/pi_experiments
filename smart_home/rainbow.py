from gpiozero import RGBLED
from time import sleep

led = RGBLED(red = 16, green = 20, blue = 21, active_high = False)

try:
	while True:
		print("red")
		led.color=(1,0,0)
		sleep(1)

		print("green")
		led.color=(0,1,0)
		sleep(1)

		print("blue")
		led.color=(0,0,1)
		sleep(1)

		print("purple")
		led.color=(1, 0, 1)
		sleep(1)

		print("cyan")
		led.color = (0, 0.5, 0.5)
		sleep(1)

		print("yellow")
		led.color = (0.4, 0.5, 0)
		sleep(1)

except KeyboardInterrupt:
	led.off()

