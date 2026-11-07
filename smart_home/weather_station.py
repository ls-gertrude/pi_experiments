import time
import board
import adafruit_dht
from rpi_lcd import LCD

dht = adafruit_dht.DHT11(board.D17)

lcd = LCD()

try:
	while True:
		try:
			temperature = dht.temperature
			humidity = dht.humidity

			if temperature is not None and humidity is not None:
				print(f"Temperature: {temperature:.1f}'C")
				print(f"Humidity: {humidity:.1f}%")

				lcd.text(f"Temp: {temperature:.1f} C", 1)
				lcd.text(f"Humidity: {humidity:.1f}%", 2)

		except RuntimeError as error:
			print(f"Sensor Reading: {error}")
		time.sleep(2)

except KeyboardInterrupt:
	print("\n Weather Station stopped.")

finally:
	lcd.clear()
	dht.exit() 
