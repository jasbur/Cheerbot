import os
import time
import subprocess
import random

# This file is what I use on my own device. It uses ServoBlaster from
# https://github.com/richardghirst/PiBits/tree/master/ServoBlaster to control
# two servos connected to a Raspberry Pi (on GPIO pins 4 and 17) to move the
# head and arm of the physical robot in sync with audio samples.

# Center the two servos I'll be using for the animations below
def center_servos():
    os.system('echo 0=50% > /dev/servoblaster')
    os.system('echo 1=100% > /dev/servoblaster')

# Play one of the contained animations randomly. Called after a successful
# cheer condition is met
def play_animation():
    animation_number = random.randint(0, 1)

    # A pretty basic bugle call and CHARGE! cheer
    if animation_number == 0:
        for i in range(2):
            subprocess.Popen(['aplay', '/home/pi/cheerbot_app/bugle_cheer.wav'])

            os.system('echo 0=85% > /dev/servoblaster')
            time.sleep(1.6)
            os.system('echo 0=50% > /dev/servoblaster')
            time.sleep(0.9)
            os.system('echo 0=15% > /dev/servoblaster')
            time.sleep(1.0)
            os.system('echo 0=50% > /dev/servoblaster')

            time.sleep(1.6)

            os.system('echo 1=15% > /dev/servoblaster')

            time.sleep(2.0)

            os.system('echo 1=80% > /dev/servoblaster')

    # A cheer that involved an audio file I don't have the right to distribute
    if animation_number == 1:
        for i in range(3):
            # subprocess.Popen(['aplay', '/home/pi/cheerbot_app/Go-Pack-Go.wav'])

            time.sleep(0.2)

            os.system('echo 0=80% > /dev/servoblaster')
            time.sleep(0.5)
            os.system('echo 0=10% > /dev/servoblaster')
            time.sleep(0.5)
            os.system('echo 0=80% > /dev/servoblaster')
            time.sleep(0.5)
            os.system('echo 0=50% > /dev/servoblaster')

            time.sleep(0.8)

            os.system('echo 1=20% > /dev/servoblaster')
            time.sleep(0.5)
            os.system('echo 1=70% > /dev/servoblaster')
            time.sleep(0.5)
            os.system('echo 1=20% > /dev/servoblaster')
            time.sleep(0.6)
            os.system('echo 1=80% > /dev/servoblaster')

            time.sleep(0.15)
