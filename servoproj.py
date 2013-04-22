import time, sys, RPi.GPIO as GPIO

# These are the pins that are attached to the switches
inputpin1 = 22
inputpin2 = 26

# This sets up the GPIO for our inputs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputpin1, GPIO.IN)
GPIO.setup(inputpin2, GPIO.IN)

# This function turns both servos to the given angle
# Note how flush is used to clear the character buffer. The servos would not move without this.
def set(value):
	print '0=' + str(value)
	sys.stdout.flush()
	time.sleep(0.01)
	print '2=' + str(value)
	sys.stdout.flush()	

delay = 0.01	# frequency for checking inputs
angle = 120	# starting angle

sys.stdout = open('/dev/servoblaster', 'w')	# opens a filestream for writing to the servos

while True:
	time.sleep(delay)
	try:
		# checks inputs
		inpA = GPIO.input(inputpin1)
		inpB = GPIO.input(inputpin2)
		if inpA:
			angle+=1
		if inpB:
			angle-=1
		# updates servos
		set(angle)
	# catches ctrl+C on the keyboard, script may not stop over ssh connection without this.
	except KeyboardInterrupt:
		sys.exit()
