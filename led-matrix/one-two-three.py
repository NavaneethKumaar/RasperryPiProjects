#!/usr/bin/env python
import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT,LCD_FONT,SEG7_FONT,SINCLAIR_FONT,SPECCY_FONT,UKR_FONT

def animation(device,num,from_y, to_y):
    '''Animate the whole thing, moving it into/out of the abyss.'''
    hourstime = datetime.now().strftime('%H')
    mintime = datetime.now().strftime('%M')
    with canvas(device) as draw:
        text(draw, (1, 0), str(num), fill="white", font=proportional(UKR_FONT))
        time.sleep(0.1)


def one_two_three(device):
    for i in range(900,1000):
        animation(device,i+1,8,0)

def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=False)
    device.contrast(8) #16

    one_two_three(device)
    


    
if __name__ == "__main__":
    main()
