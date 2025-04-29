import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def adc():
    for i in range(256):
        list = decimal2binary(i)
        for k in range(len(list)):
            GPIO.output(dac[k], list[k])
        time.sleep(0.001)
        if(GPIO.input(comp) == 0):
            return i


try:
    while(True):
        level = adc()
        voltage = (level/255)*3.3
        print(f"числовое значение: {level}, напряжение: {voltage:.2f}V")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
