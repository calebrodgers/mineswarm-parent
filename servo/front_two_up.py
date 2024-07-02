from gpiozero import AngularServo
from time import sleep

servo3 = AngularServo(19, min_pulse_width=0.0005, max_pulse_width=0.0025)

servo3.angle = -50
sleep(2)