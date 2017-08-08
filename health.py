# *****************************************************************************
# * Programmer: Karl N. King
# *****************************************************************************
# * Description: A program that emulates healthpotion in a video game. 
# *****************************************************************************
# * History: KNK (8/6/2017) - Genesis                                                 
#
# *****************************************************************************
from random import *

health = 50
difficutly = 3  # Difficutly scale: 1(easy), 2(medium), 3(hard)


potion_health = int(randint(25,50) / difficutly)

health += potion_health
print("Current HP: ", health)

