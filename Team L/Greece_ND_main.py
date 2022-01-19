from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

sense.show_message("Kalimera")
sense.show_message("My name should be Alan Turing", scroll_speed = 0.05)

humidity = sense.get_humidity()
humidity = round(humidity)
sense.show_message(str(humidity))
G= (0, 255, 0)

Green_Matrix = [
G,G, G, G, G, G, G, G,
G,G, G, G, G, G, G, G,
G,G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
]
sense.set_pixels(Green_Matrix )
