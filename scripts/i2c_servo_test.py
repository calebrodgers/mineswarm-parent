from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)

while True:
	print("Moving to 0")
	kit.servo[0].angle = 0
	kit.servo[1].angle = 0
	kit.servo[2].angle = 0
	kit.servo[3].angle = 0
	sleep(2)
	print("Moving to 180")
	kit.servo[0].angle = 180
	kit.servo[1].angle = 180
	kit.servo[2].angle = 180
	kit.servo[3].angle = 180
	sleep(2)
