from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def greece_flag():
    B = blue
    O = nothing
    W = white
    G = green
    Y = yellow
    flag = [
    B, B, W, B, B, B, B, B,
    B, B, W, B, B, W, W, W,
    W, W, W, W, W, B, B, B,
    B, B, W, B, B, W, W, W,
    B, B, W, B, B, B, B, B,
    W, W, W, W, W, W, W, W,
    B, B, B, B, B, B, B, B,
    W, W, W, W, W, W, W, W,
    ]
    return flag

def northafrica_flag():
    G = green
    R = red
    O = nothing
    B = blue
    W = white
    Y = yellow 
    flag = [
    G, W, R, R, R, R, R, R, 
    Y, G, W, R, R, R, R, R,
    O, Y, G, W, W, W, W, W, 
    O, O, Y, G, G, G, G, G,
    O, O, Y, G, G, G, G, G,
    O, Y, G, W, W, W, W, W,
    Y, G, W, B, B, B, B, B,
    G, W, B, B, B, B, B, B,
    ]
    return flag

def plus():
    W = white
    O = nothing
    flag = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return flag

def equals():
    W = white
    O = nothing
    flag = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return flag

def heart():
    P = pink
    O = nothing
    flag = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return flag

images = [greece_flag, greece_flag, plus, northafrica_flag, northafrica_flag, equals, heart, heart]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
