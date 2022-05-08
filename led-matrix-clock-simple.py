import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT,LCD_FONT,SEG7_FONT

def minute_change(device):
    '''When we reach a minute change, animate it.'''
    hours = datetime.now().strftime('%H')
    minutes = datetime.now().strftime('%M')

    def helper(current_y):
        with canvas(device) as draw:
            text(draw, (0, 1), hours, fill="white", font=proportional(CP437_FONT))
            text(draw, (15, 1), ":", fill="white", font=proportional(TINY_FONT))
            text(draw, (17, current_y), minutes, fill="white", font=proportional(CP437_FONT))
        time.sleep(0.1)
    for current_y in range(1, 9):
        helper(current_y)
    minutes = datetime.now().strftime('%M')
    for current_y in range(9, 1, -1):
        helper(current_y)


def main():
    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=False)
    device.contrast(8) #16


    toggle = False  # Toggle the second indicator every second
    while True:
        toggle = not toggle
   
        hours = datetime.now().strftime('%H')
        minutes = datetime.now().strftime('%M')
        seconds = datetime.now().strftime('%S')
        with canvas(device) as draw:
            thisFont=proportional(SEG7_FONT)
            text(draw, (1, 0), hours, fill="white", font=thisFont)
            text(draw, (9, 1), ":" if toggle else " ", fill="white", font=proportional(TINY_FONT))
            text(draw, (12, 0), minutes, fill="white", font=thisFont)
            text(draw, (21, 1), ":" if toggle else " ", fill="white", font=proportional(TINY_FONT))
            text(draw, (24, 0), seconds, fill="white", font=thisFont)
        time.sleep(0.6)


if __name__ == "__main__":
    main()
