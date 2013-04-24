import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BOARD)

pin = 26
GPIO.setup(pin, GPIO.IN)

#sys.stdout = open('/dev/servoblaster', 'w')

print '0=20'
sys.stdout.flush()
time.sleep(0.1)
print '0=220'
sys.stdout.flush()

index = 0

def smoother(value, array, index):
	#index += 1
	#if (index >= bufferlength): index = 0
	array[index] = value
	return sum(array)/len(array)

bufferlength = 3
array = [120] * bufferlength

min = 1000000
max = -1000000

while True:
	try:
		counter = 0
		if (GPIO.input(pin)):
			#This measures the width of the pulse
			while(GPIO.input(pin)):
				counter += 1
				time.sleep(0.00000001)

#			#This executes the smoothing function
#			index += 1
#			if index >= bufferlength: index = 0
#			angle = smoother(counter, array, index)
#			
#			#This automatically maps the range of the control to the range of the servo
#			if angle<min: min=angle
#			if angle>max: max=angle
#			range=max-min
#			if not range == 0:
#				mult=250/range
#				angle = int(mult*(angle - min))

			#This turns the servo
#			print angle
			print counter
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit()
