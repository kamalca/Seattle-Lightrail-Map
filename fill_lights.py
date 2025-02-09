import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 50)
for i in range(len(pixels)):
    pixels[i] = (255,0,0)
