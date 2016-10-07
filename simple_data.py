#!/usr/bin/python
import sys 
import time
from sense_hat import SenseHat


sense = SenseHat()
temp = sense.get_temperature()
temp = round(temp, 1)

sense.show_message(str(temp), text_colour=[255, 0, 0])