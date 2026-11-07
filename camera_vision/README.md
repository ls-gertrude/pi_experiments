#  Camera Vision & Motion Tracking

This folder is all about giving my Raspberry Pi eyes! I wanted to see if I could build a smart security camera setup that actually works in real life.

## The Scripts
*   `sentinel.py`: This is my main security script. It uses a PIR motion sensor to detect when someone is around. Once it spots movement, it triggers a USB webcam to snap a photo of the area.
*   `camera_test.py`: Just a quick diagnostic script I wrote to test the webcam feed and make sure the OpenCV rendering was working before I built the main system.

##  How It Works
Basically, the PIR sensor acts as the trigger. Once it picks up motion, the GPIO pins fire off an interrupt, the Python script wakes up the camera, takes a timestamped picture, and logs it.
