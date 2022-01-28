#Leei na paei sti vivliothiki kai na diavasei to vivlio SenseHat
from sense_hat import SenseHat
#Deinei onoma sto SenseHat
sense = SenseHat()
#Gyrnaei ta grammata orizontia
sense.set_rotation(270)

#Deixnei to minima stin othoni
sense.show_message("Do you like space?")

#Metatrepei tous arithmous tis ygrasias se grammata kai ta deixnei stin othoni
sense.show_message(str(sense.humidity))

