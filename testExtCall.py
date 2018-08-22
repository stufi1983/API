import subprocess
import os

os.system('omxplayer -o both /usr/share/sounds/alsa/Front_Left.wav &')
os.system('omxplayer -o both /usr/share/sounds/alsa/Front_Right.wav &')
do = subprocess.Popen(['aplay', '/usr/share/sounds/alsa/Front_Left.wav'])
re = subprocess.Popen(['aplay', '/usr/share/sounds/alsa/Front_Right.wav'])
