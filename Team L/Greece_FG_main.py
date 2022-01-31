from sense_hat import SenseHat
sense =SenseHat()
sense.set_rotation(270)
sense.show_message(" Hellas ")
sense.show_message(" Humidity 15")
a=sense.get_humiditi()
a=round (a)
sense.show_message(str(a))

O = (0,0,0)
B=(0,0,255)
R=(255,0,0)
#X =(64,64,64)
G=(0,255,0)
W = (255,255, 255)


greek_flag = [
  
B, B, W, B, B, B, B, B,
B, B, W, B, B, W, W, W,
W, W, W, W, W, B, B, B,
B, B, W, B, B, W, W, W,
B, B, W, B, B, B, B, B,
W, W, W, W, W, W, W, W,
B, B, B, B, B, B, B, B,
W, W, W, W, W, W, W, W,
]

sense.set_pixels(greek_flag)
