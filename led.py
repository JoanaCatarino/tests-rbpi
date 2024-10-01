# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:45:06 2024

@author: JoanaCatarino
"""

from gpio_map import *
from time import sleep

def blueLED():
    led.on()
    sleep(1)
    led.off()