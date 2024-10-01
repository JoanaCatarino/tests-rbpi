# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:45:04 2024

@author: JoanaCatarino
"""

import sys
import numpy as np
from PyQt5 import QtWidgets, QtCore


def generate_white_noise(duration, sample_rate=44100, amplitude=0.1):
    samples = np.random.normal(0, amplitude, int(sample_rate * duration))
    return samples


async def white_noise(self):
    sample_rate = 44100  # Sample rate in Hz
    duration = 2  # Duration in seconds
    sound = generate_white_noise(duration, sample_rate)
    await play_sound(sound, sample_rate)

