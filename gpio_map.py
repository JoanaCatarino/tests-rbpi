# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:41:47 2024

@author: JoanaCatarino
"""

from gpiozero import LED

led = LED(22)

__all__ = ['led']