from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)

sense.show_message("my name should be William Thompson ")

sense.show_message("Do you like space?")

sense.show_message("The humidity is ")
a = sense.get_humidity()
a = round(a)
sense.show_message(str(a))
sense.show_message("%")

R = (0, 0,255)
G = (255, 0, 0)
Y = (255, 255, 0)

Red_Matrix = [
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, G, R, R, R, R, G, R,
G, G, G, R, R, G, G, G,
G, G, G, G, G, G, G, G,
R, G, G, G, G, G, G, R,
R, R, G, G, G, G, R, R,
R, R, R, G, G, R, R, R,
]

sense.set_pixels(Red_Matrix)

sleep(1)

Star_Matrix = [
Y, Y, Y, R, R, Y, Y, Y,
Y, Y, R, G, G, R, Y, Y,
R, R, R, G, G, R, R, R,
R, G, G, G, G, G, G, R,
Y, R, G, G, G, G, R, Y,
R, G, G, G, G, G, G, R,
R, G, G, R, R, G, G, R,
R, R, R, G, G, R, R, R,
]

sense.set_pixels(Star_Matrix)
