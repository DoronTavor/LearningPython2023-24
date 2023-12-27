import math  # built-in module
from math import pi
import sys
import random as rdm
from enum import Enum
import kansas
from rps_lesson_14 import rock_paper_scissors

print(math.pi)
print(pi)
print(rdm.choice("123456789"))

# for item in dir(rdm):
#     print(item)

print(kansas.capital)
kansas.randomfunfact()
print(__name__)
print(kansas.__name__)

rock_paper_scissors()
sys.exit("BYE")
