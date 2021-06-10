import board
import busio

'''
Read i2c devices attached to a microcontroller.
'''

REGISTERS = (0, 7)  # Range of registers to read, from the first up to (but
                      # not including!) the second value.

REGISTER_SIZE = 1     # Number of bytes to read from each register.
reg_types = {0:'SEC', 1:'MIN', 2:'HOUR', 3: 'WK_DAY', 4: 'DATE', 5: 'MONTH', 6: 'YEAR'}
datetime = {'SEC':0, 'MIN':0, 'HOUR':0, 'WK_DAY':0, 'DATE':0, 'MONTH':0, 'YEAR':0}

# Initialize and lock the I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)
while not i2c.try_lock():
	pass

# Scan all the registers and read their byte values.
def get_datetime():

	# Find the first I2C device available.
	devices = i2c.scan()
	while len(devices) < 1: 
	    devices = i2c.scan()
	device = devices[0]

	result = bytearray(REGISTER_SIZE)
	for register in range(*REGISTERS):
	    try:
	        #i2c.writeto(device, bytes([register]))
	        i2c.readfrom_into(device, result)
	    except OSError:
	        continue  # Ignore registers that don't exist!
	    val = hex(result[0])[2:]
	    datetime[reg_types[register]] = val
	human_datetime = '20{0}-{1}-{2}; {3}:{4}:{5}h'.format(datetime['YEAR'], datetime['MONTH'], datetime['DATE'], datetime['HOUR'], datetime['MIN'], datetime['SEC'])

	# Unlock the I2C bus when finished.  Ideally put this in a try-finally!

	return human_datetime