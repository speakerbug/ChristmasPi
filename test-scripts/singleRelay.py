import RPi.GPIO as GPIO, time

pin = 11

GPIO.setmode(GPIO.BOARD)
print("Getting Started")
time.sleep(3.0)

print("Turning on 1")
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, True)
time.sleep(2.0)
print("Turning off 1")
GPIO.output(pin, False)

GPIO.cleanup()