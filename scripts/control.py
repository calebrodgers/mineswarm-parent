import serial
import json
import time
import sys
import math

ser = serial.Serial('/dev/ttyS0',115200,timeout=1)

# take in coordinates of area to be searched
# break up into areas to be searched by children
# drive to child deployment locations
# deploy children 

#later: ADJUST PLAN BASED ON LOCATIONS OF MINES

def main():
	angle_time = abs(float(sys.argv[1])) / 50
	if float(sys.argv[1]) > 0:
	    data = {"T":1,"L":-0.1,"R":0.1}
	else:
	    data = {"T":1,"L":0.1,"R":-0.1}
	stop_data = {"T":1,"L":0.0,"R":0.0}
	json_data = json.dumps(data).encode("utf-8")
	json_stop_data = json.dumps(stop_data).encode("utf-8")
	print("turning")
	ser.write(json_data+ b'\n')
	print(angle_time)
	ser.write(json_data+ b'\n')
	time.sleep(angle_time)
	ser.write(json_stop_data+ b'\n')

	dist_time = float(sys.argv[2])

	print("driving")
	data = {"T":1,"L":-0.1,"R":-0.1}
	json_data = json.dumps(data).encode("utf-8")
	for i in range(math.floor(dist_time)):
	    ser.write(json_data+ b'\n')
	    time.sleep(1)
	time.sleep(dist_time-math.floor(dist_time))
	
#	while True:
#		data1 = {"T":1,"L":0.5,"R":0.5}
#		data2 = {"T":1,"L":0,"R":0}
#		json_data1 = json.dumps(data1).encode("utf-8")
#		json_data2 = json.dumps(data2).encode("utf-8")
#		ser.write(json_data1+ b'\n')
#		time.sleep(3)
#		ser.write(json_data2+ b'\n')
#		time.sleep(3)
		

if __name__ =="__main__":
	main()
