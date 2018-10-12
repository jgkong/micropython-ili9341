# test of printing multiple fonts to the ILI9341 on an M5Stack using H/W SP
# MIT License; Copyright (c) 2017 Jeffrey N. Magee

from ili934xnew import ILI9341, color565
from machine import Pin, SPI
import glcdfont
import tt14
import tt24
import tt32

fonts = [glcdfont,tt14,tt24,tt32]

text = 'Now is the time for all good men to come to the aid of the party.'


#power = Pin(m5stack.TFT_LED_PIN, Pin.OUT)
#power.value(1)

baudrate = 32000000
print('Baudrate = {}'.format(baudrate))
print(text)

spi = SPI(
    2,
    baudrate=baudrate,
    miso=Pin(15),
    mosi=Pin(18),
    sck=Pin(5))

display = ILI9341(
    spi,
    cs=Pin(23),
    dc=Pin(19),
    rst=Pin(21))
display.erase()
display.set_pos(0,0)
for ff in fonts:
    display.set_font(ff)
    display.print(text)


