#!/usr/bin/python
import sys 
import time
from sense_hat import SenseHat


sense = SenseHat()
temp = sense.get_temperature()
sense.show_message(str(temp), text_colour=[255, 0, 0])