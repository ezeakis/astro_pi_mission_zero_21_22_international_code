from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
sense.show_message("my name should be William Thompson ")


sense.show_message("Humidity is ")


a = sense.get_humidity()
a = round(a)
sense.show_message(str(a))

R = (0, 0,255)
G = (255, 0, 0)

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


