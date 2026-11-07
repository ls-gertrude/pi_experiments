# Smart Home & Physical Security

This is where I keep all the scripts that interface directly with my physical electronic components. It got complex and a bit confusing but eventually, I got the hang of it!

## What I Built
*   `vault.py`: A physical security vault! You have to type the right passcode on a 4x4 matrix keypad, and the status shows up on a 16x2 LCD. The best part? If someone enters the wrong code it locks for about 30 seconds.
*   `weather_station.py`: A script to track environmental conditions.
*   `security.py` & `doorbell.py` (plus `doorbellsound.py`): Scripts for perimeter monitoring using active buzzers.
*   `motion_greeter.py`: An automated greeter using a PIR motion sensor (it has a tiny face!). It stays happy when I'm there, goes blank when I leave, and even sends me a welcome message on my Telegram.
*   *Just for fun:* `traffic_light.py`, `rainbow.py`, and `quotes.py`.

## How to run these
You can run any of these directly from the Pi terminal. For example, to fire up the vault:
```bash
python3 vault.py
