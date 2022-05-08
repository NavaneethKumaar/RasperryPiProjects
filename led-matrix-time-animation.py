import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT


def first(device):
    '''When we reach a minute change, animate it.'''
    hours = datetime.now().strftime('%H')
    minutes = datetime.now().strftime('%M')

    for current_y in range(9, 1, -1):
        with canvas(device) as draw:
            text(draw, (0, current_y), hours, fill="white", font=proportional(CP437_FONT))
            text(draw, (15, current_y), ":", fill="white", font=proportional(TINY_FONT))
            text(draw, (17, current_y), minutes, fill="white", font=proportional(CP437_FONT))
        time.sleep(0.1)

def minute_change(device):
    '''When we reach a minute change, animate it.'''
    hours = datetime.now().strftime('%H')
    minutes = datetime.now().strftime('%M')

    for current_y in range(1, 9):
        with canvas(device) as draw:
            text(draw, (0, current_y), hours, fill="white", font=proportional(CP437_FONT))
            text(draw, (16, current_y), ":", fill="white", font=proportional(TINY_FONT))
            text(draw, (18, current_y), minutes, fill="white", font=proportional(CP437_FONT))
        time.sleep(0.1)

    minutes = datetime.now().strftime('%M')
    for current_y in range(9, 1, -1):
        with canvas(device) as draw:
            text(draw, (0, current_y), hours, fill="white", font=proportional(CP437_FONT))
            text(draw, (16, current_y), ":", fill="white", font=proportional(TINY_FONT))
            text(draw, (18, current_y), minutes, fill="white", font=proportional(CP437_FONT))
        time.sleep(0.1)



def main():
    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=False)
    device.contrast(8) #16


    first(device)

    toggle = False  # Toggle the second indicator every second
    while True:
        toggle = not toggle
        hours = datetime.now().strftime('%H')
        minutes = datetime.now().strftime('%M')
        with canvas(device) as draw:
            text(draw, (1, 1), hours, fill="white", font=proportional(CP437_FONT))
            text(draw, (16, 1), ":" if toggle else " ", fill="white", font=proportional(TINY_FONT))
            text(draw, (18, 1), minutes, fill="white", font=proportional(CP437_FONT))
        time.sleep(0.5)
            
        sec = datetime.now().second
        if sec == 59 or sec == 10 or sec == 20 or sec == 30 or sec == 40 or sec == 50:
            # When we change minutes, animate the minute change
            minute_change(device)




if __name__ == "__main__":
    main()
