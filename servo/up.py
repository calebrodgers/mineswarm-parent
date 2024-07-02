from gpiozero import AngularServo
from time import sleep
import sys

if '1' in sys.argv:
    print('Deploying Platform 1')
    servo1 = AngularServo(19, min_pulse_width=0.0005, max_pulse_width=0.0025)
    servo1.angle = -30
if '2' in sys.argv:
    print('Deploying Platform 2')
    servo2 = AngularServo(13, min_pulse_width=0.0005, max_pulse_width=0.0025)
    servo2.angle = 50
if '3' in sys.argv:
    print('Deploying Platform 3')
    servo3 = AngularServo(18, min_pulse_width=0.0005, max_pulse_width=0.0025)
    servo3.angle = -50
if '4' in sys.argv:
    print('Deploying Platform 4')
    servo4 = AngularServo(12, min_pulse_width=0.0005, max_pulse_width=0.0025)
    servo4.angle = 30





sleep(1)
