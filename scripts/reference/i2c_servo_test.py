from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)

while True:
	print("Moving up")
	kit.servo[0].angle = 20
	kit.servo[1].angle = 20
	kit.servo[2].angle = 100
	kit.servo[3].angle = 0
	sleep(2)
	print("Moving down")
	kit.servo[0].angle = 0
	kit.servo[1].angle = 100
	kit.servo[2].angle = 180
	kit.servo[3].angle = 180
	sleep(2)
