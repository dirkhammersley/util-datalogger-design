import busio
import board
import time
import neopixel
import digitalio

#setup hardware LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

#Neopixel setup
'''
pixel_pin = board.NEOPIXEL
num_pixels = 1
pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, OFF = (255, 0, 0), (255, 150, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (180, 0, 255), (0, 0, 0)
pixel.fill(PURPLE)
pixel.show()
'''

# Initialize and lock the I2C bus.
print("initializing i2c...")

i2c = busio.I2C(board.D7, board.D6)
print("trying to lock i2c bus...")

while not i2c.try_lock():
	pass
print("i2c bus locked!")
print("scanning for devices...")
devices = i2c.scan()
while len(devices) < 1: 
	devices = i2c.scan()
print(devices)

while True:
	led.value = True
	time.sleep(0.5)
	led.value = False
	time.sleep(0.5)