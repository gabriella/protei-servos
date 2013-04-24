#This file lets the user choose between autonomous mode and RC mode

relay0 = 12
relay1 = 22
input = 26
cutoff = 63

import RPi.GPIO as GPIO, sys, time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay0, GPIO.OUT)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(input, GPIO.IN)

angle = 0
#Initialize the smoother
bufferlength = 3
array = [68] * bufferlength
index = 0
#Initialize Servoblaster. Make sure /pi/home/PiBits/Servoblaster/servod is run
sys.stdout = open('/dev/servoblaster', 'w')

while True:
	try:
		#First, check which mode is being used
		counter=0
		if (GPIO.input(input)):
			while(GPIO.input(input)):
				counter += 1
				time.sleep(0.00000001)
			#Automatic Smoother
			index = (index+1)%bufferlength
			array[index] = counter
			counter = sum(array)/len(array)
		
			if (counter > cutoff):
				#Run using RC mode
				GPIO.output(relay0, GPIO.HIGH)
				GPIO.output(relay1, GPIO.LOW)
				#print 'RC'
				
					
			else:
				#Run using autonomous mode
				GPIO.output(relay0, GPIO.LOW)
				GPIO.output(relay1, GPIO.HIGH)
				#print 'AUTO'
				angle = (angle+3)%250
				print '0=' + str(angle)
				sys.stdout.flush()

	except KeyboardInterrupt:
		sys.exit()
