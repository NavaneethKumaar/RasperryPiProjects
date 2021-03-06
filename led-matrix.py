import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT


def output(n, block_orientation, rotate, inreverse, text):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    print(text)

    #show_message(device, text, fill="white", font=proportional(CP437_FONT), scroll_delay=0.05)
    show_message(device, text, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)
    time.sleep(1)


#main
while True: # loop
    name=input("Enter Your Name: ")
    output(4, 90, 0,True,name)
 
