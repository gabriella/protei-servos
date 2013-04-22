import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BOARD)

pin = 26
GPIO.setup(pin, GPIO.IN)

sys.stdout = open('/dev/servoblaster', 'w')

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

bufferlength = 25
array = [0] * bufferlength

while True:
	try:
		counter = 0
		if (GPIO.input(pin)):
			while(GPIO.input(pin)):
				counter += 1
				time.sleep(0.00000001)
			angle = int(counter * 5.581 - 235)

			index += 1
			if index >= bufferlength: index = 0
			angle = smoother(angle, array, index)

			print '0=' + str(angle)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit()
