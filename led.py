# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:45:06 2024

@author: JoanaCatarino
"""

from gpio_map import *
import asyncio

async def blueLED():
    blueLED.on()
    await asyncio.sleep(1)
    blueLED.off()