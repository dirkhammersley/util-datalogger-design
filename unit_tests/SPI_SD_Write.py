import busio
import board
import digitalio
import struct
import adafruit_sdcard
import storage
import os

SD_CS = board.D14
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(SD_CS)
sd_card = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sd_card)
storage.mount(vfs, "/sd")
with open("/sd/test.txt", "w") as f:
    f.write("Hello world!\r\n")