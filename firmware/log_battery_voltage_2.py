import busio
import board
import digitalio
import analogio
import time
import sdmount
import ds3231
import storage
import neopixel

'''
-Read analog voltage from battery and log to SD card along with timestamp
-Each second by CPU time, record "CPU timestamp: "
-Each second by RTC time, record "RTC timestamp: "
-Pulse or blink the LED
'''

#Analog read setup
analog_in = analogio.AnalogIn(board.A5)

#setup hardware LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

#Neopixel setup
pixel_pin = board.NEOPIXEL
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, OFF = (255, 0, 0), (255, 150, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (180, 0, 255), (0, 0, 0)

 #Read analog voltage
def get_voltage(pin):
    return (pin.value * 3.3) / 65536
 
#SD Card setup
#SD_CS = board.D14
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#cs = digitalio.DigitalInOut(SD_CS)
#sd_card = adafruit_sdcard.SDCard(spi, cs)
#vfs = storage.VfsFat(sd_card)
#storage.mount(vfs, "/sd")

#print basic info and the time
#current = rtc.datetime
find_i2c_devices()
print("Utility Datalogger, revB")
print("Log start time: ")
#print(time_from_struct_time(current))

#loop
with open("/sd/test.log", "a") as f:
	f.write("Log begins..................\n")
	while True:
		cpu_time = (time.monotonic())
		rtc_time = ds3231.get_datetime()
		v_read = get_voltage(analog_in)
		out_string = "CPU time: " + str(cpu_time) + ", RTC time" + rtc_time + ", V_in: " + str(v_read) + "\n"
		print(out_string)
		f.write(out_string)
		led.value = True
		time.sleep(0.5)
		led.value = False
		time.sleep(0.5)