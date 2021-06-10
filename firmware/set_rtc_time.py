import board
import busio
import adafruit_ds3231
import time

i2c = busio.I2C(board.SCL, board.SDA)
rtc = adafruit_ds3231.DS3231(i2c)

YEAR = 2020
MONTH = 06
DAY = 07
HOUR = 16
MIN = 23
SEC = 00
DAY_OF_WEEK = 06
DAY_OF_YEAR = 159
IS_DAYLIGHT_SAV_TIME = 1

rtc.datetime = time.struct_time((YEAR, MONTH, DAY, HOUR, SEC, DAY_OF_WEEK, DAY_OF_YEAR, IS_DAYLIGHT_SAV_TIME))
print("Success! RTC time set to: ")
print(rtc.datetime)
