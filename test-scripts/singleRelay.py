import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
print("Getting Started")
time.sleep(3.0)

print("Turning on 1")
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, True)
time.sleep(2.0)
print("Turning off 1")
GPIO.output(11, False)

GPIO.cleanup()
