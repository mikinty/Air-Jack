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
	a = int.from_bytes(ser.read(size=1), byteorder="big")
	b = int.from_bytes(ser.read(size=1), byteorder="big")
	c = int.from_bytes(ser.read(size=1), byteorder="big")
	#play sound based on a, b, c
	print(a, b, c)
	e = int.from_bytes(ser.read(size=1), byteorder="big")
	if(e != ord('e')):
		print("Something is wrong")
