import busio
import board
import digitalio
import analogio
import adafruit_sdcard
import time
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
BATT_CONVERSION = 1.72
v_bat = analogio.AnalogIn(board.A5)
alg_0 = analogio.AnalogIn(board.A0)
alg_1 = analogio.AnalogIn(board.A1)
alg_2 = analogio.AnalogIn(board.A2)

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
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(SD_CS)
sd_card = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sd_card)
storage.mount(vfs, "/sd")

#print basic info and the time
#current = rtc.datetime
print("Utility Datalogger, revB")
print("Log start time: ")
dt_tm = ds3231.get_datetime()
print(dt_tm)

#loop
f_name = "/sd/" + dt_tm + ".log"
with open(f_name, "a") as f:
	f.write("Log begins..................\n")
	f.write("[CPU time], [RTC time], [V_bat], [A0], [A1], [A2]\n")
	while True:
		cpu_time = (time.monotonic())
		rtc_time = ds3231.get_datetime()
		v_read = get_voltage(v_bat)
		out_string = "CPU time: " + str(cpu_time) + \
					", RTC time: " + rtc_time + \
					", V_bat: " + str(v_read * BATT_CONVERSION) + \
					", A0: " + str(get_voltage(alg_0)) + \
					", A1:" +  str(get_voltage(alg_1)) +\
					", A2: " + str(get_voltage(alg_2)) + "\n"
		print(out_string)
		f.write(out_string)
		led.value = True
		time.sleep(0.5)
		led.value = False
		time.sleep(0.5)