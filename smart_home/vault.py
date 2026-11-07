import requests
from time import sleep
from rpi_lcd import LCD
from gpiozero import DigitalOutputDevice as Out,DigitalInputDevice as In


PIN = "1234"
lcd = LCD()
rows = [Out(p) for p in [5,6,13,19]]
cols = [In(p), pull_up=False) for p in [18,23,24,25]]
MAP = [["1", "2", "3", "A"],
       ["4", "5", "6", "B"],
       ["7", "8", "9", "C"],
       ["*", "0", "#", "D"]]

def get_key():
    for i,r in enumerate(rows):
        r.on()
        sleep(0.01)
        for j,c in enumerate(cols):
            if c.is_active:
                sleep(0.02)
                while c.is_active: pass
                r.off()
                return MAP[i][j]
        r.off()
    return None
    

buf,err = "", 0
lcd.text("Enter PIN", 1)

while True:
    k = get_key()
    if k and k.isdigit():
        buf += k
        lcd.text("*" * len(buf),2)
    elif k == "#":
        if buf == PIN:
            lcd.clear(); lcd.text("OPEN!",1)
            err = 0
        else:
            err +=1
            lcd.text(f"WRONG({err}/3",1)
            if err>=3:

                sleep(30)
                err = 0
            buf = ""
            sleep(2)
            lcd.clear(); lcd.text("Enter PIN:",1)
        sleep(0.1)
