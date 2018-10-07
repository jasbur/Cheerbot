import subprocess
import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# This is a bootstrapper to be called when you'd like score monitoring to begin.
# It will launch the main program and re-launch it if it crashes due to Internet
# weirdness regarding the JSON package exchange. If you're running the acript
# on boot with a Raspberry Pi It's best to launch a few seconds in to boot so
# the network can start ahead of it. If launching in /etc/crontab using '@reboot'
# prepend something like 'sleep 20;' before calling this script.
while True:
    ps_output = subprocess.getoutput("ps -ax")

    if script_dir + "/cheerbot.py" not in ps_output:
        # subprocess.call(['sudo', 'killall', 'servod']) ### This line is only needed if using Servoblaster to drive servos during a cheer
        subprocess.Popen(['sudo', 'python3', script_dir + '/cheerbot.py'])

    time.sleep(10.0)
