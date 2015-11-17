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

print("Turning on 4")
GPIO.setup(four, GPIO.OUT)
GPIO.output(four, True)
time.sleep(2.0)
print("Turning off 4")
GPIO.output(four, False)

print("Turning on 5")
GPIO.setup(five, GPIO.OUT)
GPIO.output(five, True)
time.sleep(2.0)
print("Turning off 5")
GPIO.output(five, False)

print("Turning on 6")
GPIO.setup(six, GPIO.OUT)
GPIO.output(six, True)
time.sleep(2.0)
print("Turning off 6")
GPIO.output(six, False)

print("Turning on 7")
GPIO.setup(seven, GPIO.OUT)
GPIO.output(seven, True)
time.sleep(2.0)
print("Turning off 7")
GPIO.output(seven, False)

print("Turning on 8")
GPIO.setup(eight, GPIO.OUT)
GPIO.output(eight, True)
time.sleep(2.0)
print("Turning off 8")
GPIO.output(eight, False)

GPIO.cleanup()