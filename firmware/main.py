import busio
import board
import time
import neopixel
import digitalio

#setup hardware LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


REGISTERS = range(0x00, 0x1E) #WHO_AM_I register, expect 0x6A
REGISTER_SIZE = 1

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

def read_register(device, register):
		result = bytearray(REGISTER_SIZE)
		try:
			i2c.writeto(device, bytes([register]))
			i2c.readfrom_into(device, result)
			print("from register ", hex(register), ": ", bin([i for i in result][0]))
		except OSError:
			pass  # Ignore registers that don't exist

read_register(0x24, 0x07)
#for register in REGISTERS:
	#read_register(0x24, register)

while True:
	while not 0x24 in devices:
		pass
	print("Found device 0x24...")
	for register in REGISTERS:
		read_register(0x24, register)

	led.value = True
	time.sleep(0.5)
	led.value = False
	time.sleep(0.5)