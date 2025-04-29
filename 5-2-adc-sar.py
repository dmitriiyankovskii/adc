import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def adc():
    list_ = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        GPIO.output(dac[i], 1)
        time.sleep(0.001)
        if(GPIO.input(comp) == 0):
            GPIO.output(dac[i], 0)
            list[i] = 0
        elif(GPIO.input(comp) == 1):
            GPIO.output(dac[i], 1)
            list[i] = 1
    for k in range(8):
        num = list_[i]*(2**(7-i))
    return num

try:
    while(True):
        num = adc()
        voltage = (num/255)*3.3
        print("числовое значение: "+num+" напряжение: "+voltage)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)