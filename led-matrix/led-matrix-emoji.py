import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT



def main():
    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=False)
    device.contrast(8) #16
    

# https://en.wikipedia.org/wiki/Code_page_437
    
    thisChar1=chr(0x1)
    thisChar2=chr(0x3)
    thisChar3=chr(0x5)
    thisChar4=chr(0x6)
    for current_x in range(32,-1,-1):
        with canvas(device) as draw:
            text(draw, (current_x, 0), thisChar1, fill="white", font=proportional(CP437_FONT))
            text(draw, (current_x + 8, 1), thisChar2, fill="white", font=proportional(CP437_FONT))
            text(draw, (current_x + 16, 0), thisChar3, fill="white", font=proportional(CP437_FONT))
            text(draw, (current_x + 24, 0), thisChar4, fill="white", font=proportional(CP437_FONT))    
        time.sleep(0.1)


if __name__ == "__main__":
    main()


