from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

sense.show_message("Save the eviroment")
sense.show_message("My name is john", scroll_speed = 0.08)

humidity = sense.get_humidity()
humidity = round(humidity)
sense.show_message(str(humidity)
R = (0, 0, 255)
G = (0, 255, 0)
B = (0, 0, 0)


RGB_Matrix = [
B,G, G, G, G, G, G, B,
B,G, G, R, G, G, G, B,
B,G, G, G, R, G, G, B,
B, G, G, G, R, G, G, G,
B, G, G, G, G, G, G, G,
