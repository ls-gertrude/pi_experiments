from gpiozero import LED
from time import sleep

red = LED(18)
yellow = LED(23)
green = LED(25)

try:
	while True:
		red.off()
		yellow.off()
		green.on()
		sleep(4)

		green.off()
		yellow.on()
		red.off()
		sleep(1.5)

		yellow.off()
		red.on()
		sleep(4)

except KeyboardInterrupt:
	red.off()
	yellow.off()
	green.off()
