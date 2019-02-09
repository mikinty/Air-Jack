import serial

port = "/dev/cu.usbserial-14410" # check if this is right
rate = 9600

ser = serial.Serial(port, rate)
ser.flushInput()

while(True):
	s = int.from_bytes(ser.read(size=1), byteorder="big")
	if(s != ord('s')):
		print("Something is wrong")
		continue
	# subtract 48 because we add 48 when sending
	# this is pretty stupid but it's hard to send e.g. 0 through serial
	# 48 because 0 + 48 == '0'
	a = int.from_bytes(ser.read(size=1), byteorder="big") - 48
	b = int.from_bytes(ser.read(size=1), byteorder="big") - 48
	c = int.from_bytes(ser.read(size=1), byteorder="big") - 48
	#play sound based on a, b, c
	print(a, b, c)
	e = int.from_bytes(ser.read(size=1), byteorder="big")
	if(e != ord('e')):
		print("Something is wrong")
