import busio
import board
import digitalio
import analogio
import time
import struct
import adafruit_sdcard
import adafruit_ds3231
import storage
import neopixel
import os

'''
-Read analog voltage from battery and log to SD card along with timestamp
-Each second by CPU time, record "CPU timestamp: "
-Each second by RTC time, record "RTC timestamp: "
-Pulse or blink the LED
'''

#i2c setup
#i2c = busio.I2C(board.SCL, board.SDA)

#setup RTC
#rtc = adafruit_ds3231.DS3231(i2c)

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
SD_CS = board.D14
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#cs = digitalio.DigitalInOut(SD_CS)
#sd_card = adafruit_sdcard.SDCard(spi, cs)
#vfs = storage.VfsFat(sd_card)
#storage.mount(vfs, "/sd")

def time_from_struct_time(rtc_time):
	return '{}/{}/{} {:02}:{:02}:{:02}'.format(rtc_time.tm_mon, rtc_time.tm_mday, rtc_time.tm_year, rtc_time.tm_hour, rtc_time.tm_min, rtc_time.tm_sec)

#print basic info and the time
#current = rtc.datetime
print("Utility Datalogger, revB")
print("Log start time: ")
#print(time_from_struct_time(current))

#loop
'''with open("/sd/test.log", "a") as f:
	f.write("Log begins..................\n")
	while True:
		cpu_time = (time.monotonic())
		#current_rtc_time = time_from_struct_time(rtc.datetime)
		v_read = get_voltage(analog_in)
		#f.write("CPU time: " + str(cpu_time) + ", RTC time" + current_rtc_time + ", V_in: " + str(v_read) + "\n")
		led.value = True
		time.sleep(0.5)
		led.value = False
		time.sleep(0.5)'''