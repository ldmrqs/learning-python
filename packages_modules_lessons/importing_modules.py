# different ways to import modules

# 1:
import how_to_create_a_module

how_to_create_a_module.hello()

#2:
import how_to_create_a_module as htcam
htcam.hello()

#3:
from how_to_create_a_module import hello #verify if the module doesn't have the same name function to avoid name clashing
hello()

#4:
from random import * #importing everything from random
randint(1, 10)

"""
the best practice for this is to import the modules using an alias, for example
import random as rdm
this will prevent name clashing and you know from where this is coming
"""