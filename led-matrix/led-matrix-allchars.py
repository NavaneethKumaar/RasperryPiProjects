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
    
    for current_y in range(1, 255, 1):
        thisChar=chr(current_y)
        for current_x in range (32,1,-1):
            with canvas(device) as draw:
                text(draw, (current_x, 0), thisChar, fill="white", font=proportional(CP437_FONT))
            time.sleep(0.1)


if __name__ == "__main__":
    main()

