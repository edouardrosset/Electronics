import serial

#Read serial S0 at 38400 bauds speed
ser = serial.Serial('/dev/ttyS0',38400)

while True:
	line = ser.readline()
	print(line)

ser.close()
