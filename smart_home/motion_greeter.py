import requests
import time
from gpiozero import MotionSensor
import pygame
import os
from dotenv import load_dotenv

load_dotenv()

telegram_token = os.getenv('BOT_TOKEN')
BOT_TOKEN = telegram_token
CHAT_ID = os.getenv('CHAT_ID')

# To send alert to my telegram
def send_alert():
	try:
		msg = "Welcome!"
		url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
	except Exception as e:
		print(f"Telegram error: {e}")

# hardware & pygame setup
pir = MotionSensor(18)
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("LOVE")

CYAN = (0, 255, 220)
BLACK = (0,0,0)

def draw_face(awake=False):
	screen.fill(BLACK)
	if awake:
		pygame.draw.circle(screen, CYAN, (200,140), 45)
		pygame.draw.circle(screen, CYAN, (400,140), 45)
		#smile
		pygame.draw.circle(screen, CYAN, (300,230), 55)
		pygame.draw.rect(screen, BLACK, (230,170,140,60))
	else:
		# Idle eyes
		pygame.draw.line(screen, CYAN, (150,160), (250,160), 10)
		pygame.draw.line(screen, CYAN, (350, 160),(450,160), 10)
		#sleeping mouth
		pygame.draw.line(screen, CYAN, (270,260), (330,260), 6)
	pygame.display.flip()

# start with sleepy face
draw_face(awake=False)
print("Welcome guard active... Waiting for motion.")

# MAIN LOOP
try:
	while True:
		pygame.event.pump()
		if pir.motion_detected:
			print("Motion detected! Waking up...")

			# wake face up
			draw_face(awake=True)
			# send telegram alert
			send_alert()
			time.sleep(6)

			draw_face(awake=False)
			print("Going back to sleep...")

		time.sleep(0.2)
except KeyboardInterrupt:
	pygame.quit()
