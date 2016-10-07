#!/usr/bin/python
import sys 
import time
from sense_hat import SenseHat


sense = SenseHat()
sense.show_message("One small step for Pi!", text_colour=[255, 0, 0])
sense.show_message("1 2 3 4 5 6 7 8 9", text_colour=[255, 0, 0])