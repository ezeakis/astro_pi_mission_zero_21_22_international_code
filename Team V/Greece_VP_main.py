from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(270)

sense.show_message("Hi:)")

sense.show_message("My name should be Daskalakis", scroll_speed = 0.07 )

sense.show_message("Humidity:")

a = sense.get_humidity()

a = round(a)

sense.show_message(str(a))

 

G = (0, 0, 0)

Y = (255, 255, 0)

R = (255, 0, 0)

Happy_Matrix = [

G, G, G, G, G, G, G, G,

G, G, Y, Y, Y, Y, G, G,

G, Y, G, Y, Y, G, Y, G,

G, Y, Y, Y, Y, Y, Y, G,

G, Y, Y, Y, G, R, R, R,

G, Y, Y, Y, G, Y, R, G,

G, G, Y, Y, Y, Y, G, G,

G, G, G, G, G, G, G, G,

]

 

sense.set_pixels(Happy_Matrix)
