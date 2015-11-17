import RPi.GPIO as GPIO, time

one = 11
two = 12
three = 13
four = 15
five = 16
six = 18
seven = 22
eight = 7

GPIO.setmode(GPIO.BOARD)
print("Getting Started")
time.sleep(3.0)

print("Turning on 1")
GPIO.setup(one, GPIO.OUT)
GPIO.output(one, True)
time.sleep(2.0)
print("Turning off 1")
GPIO.output(one, False)

print("Turning on 2")
GPIO.setup(two, GPIO.OUT)
GPIO.output(two, True)
time.sleep(2.0)
print("Turning off 2")
GPIO.output(two, False)

print("Turning on 3")
GPIO.setup(three, GPIO.OUT)
GPIO.output(three, True)
time.sleep(2.0)
print("Turning off 3")
GPIO.output(three, False)

GPIO.cleanup()