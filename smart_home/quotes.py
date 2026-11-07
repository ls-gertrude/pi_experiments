import random
import time

quotes = [ "Viva La Vida", "It might not seem like it but you'll be fine",
           "With God, all things are possible", "You can do it, fighting!!",
           "one line at a time, you'll build the next big thing", "Que Sera, Sera",
           "Life is a jouney of daily consistent steps, keep moving!", "life is a jouney of faith",
           "Faith says I know it will work", "this is you telling you, you can do it!!",
           "Do it now!!", "You'll reach there, don't worry, keep moving"]

print("---DAILY QUOTES---")
time.sleep(0.5)

daily = random.choice(quotes)

print("\n" + "*" * 35)
print(daily)
print("*" * 35)

input("press enter to activate")


