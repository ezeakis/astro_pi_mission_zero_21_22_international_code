from sense_hat import SenseHat
cookie=SenseHat()
cookie.set_rotation(270)

cookie.show_message("Be strong")



cookie.show_message("Humidity is")

a = cookie.get_humidity()
a = round(a)
cookie.show_message(str(a))
