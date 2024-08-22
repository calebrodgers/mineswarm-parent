from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)

while True:
	print("Moving up")
	kit.servo[0].angle = 110
	kit.servo[1].angle = 170
	kit.servo[2].angle = 170
	kit.servo[3].angle = 110
	sleep(2)
	print("Moving down")
	kit.servo[0].angle = 170
	kit.servo[1].angle = 110
	kit.servo[2].angle = 110
	kit.servo[3].angle = 170
	sleep(2)
