import RPi.GPIO as GPIO, sys, time

pin = [7,11,13,12,15,16,18,22]
more = [8,10,19,21,23,24,26]
#pin = int(sys.argv[1])
#pin2 = int(sys.argv[2])
GPIO.setmode(GPIO.BOARD)

for o in more:
	GPIO.setup(o, GPIO.IN)

for o in pin:
	GPIO.setup(o, GPIO.IN)
#GPIO.setup(pin, GPIO.IN)
#GPIO.setup(pin2, GPIO.IN)
#GPIO.setup(22, GPIO.IN)

while True:
	try:
		time.sleep(0.2)
		for o in more:
			inpval = GPIO.input(o)
			print "Pin " + str(o) + ": " + str(inpval)
		for o in pin:
			inpval = GPIO.input(o)
			print "Pin " + str(o) + ": " + str(inpval)
	except KeyboardInterrupt:
		sys.exit()
