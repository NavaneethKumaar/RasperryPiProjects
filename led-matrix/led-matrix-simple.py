#!/usr/bin/env python
import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT,LCD_FONT,SEG7_FONT,SINCLAIR_FONT,SPECCY_FONT,UKR_FONT

def animation(device, from_y, to_y):
    '''Animate the whole thing, moving it into/out of the abyss.'''
    hourstime = datetime.now().strftime('%H')
    mintime = datetime.now().strftime('%M')
    current_y = from_y
    while current_y != to_y:
        with canvas(device) as draw:
            text(draw, (19, current_y), "R", fill="white", font=proportional(UKR_FONT))
#             text(draw, (8, current_y), "A", fill="white", font=proportional(UKR_FONT))
#             text(draw, (16, current_y), "S", fill="white", font=proportional(UKR_FONT))
#             text(draw, (24, current_y), "P", fill="white", font=proportional(UKR_FONT))
        time.sleep(0.1)
        current_y += 1 if to_y > from_y else -1

#     while current_y != to_y:
#         with canvas(device) as draw:
#             text(draw, (0, current_y), hourstime, fill="white", font=proportional(CP437_FONT))
#             text(draw, (15, current_y), ":", fill="white", font=proportional(TINY_FONT))
#             text(draw, (17, current_y), mintime, fill="white", font=proportional(CP437_FONT))
#         time.sleep(0.1)
#         current_y += 1 if to_y > from_y else -1


def main():
    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=False)
    device.contrast(8) #16

    # The time ascends from the abyss...
    animation(device, 8, 0)
    
#     toggle = False  # Toggle the second indicator every second
#     while True:
#         toggle = not toggle
#         hours = datetime.now().strftime('%H')
#         minutes = datetime.now().strftime('%M')
#         with canvas(device) as draw:
#             text(draw, (0, 1), hours, fill="white", font=proportional(CP437_FONT))
#             text(draw, (15, 1), ":" if toggle else " ", fill="white", font=proportional(TINY_FONT))
#             text(draw, (17, 1), minutes, fill="white", font=proportional(CP437_FONT))
#         time.sleep(0.5)


    
if __name__ == "__main__":
    main()