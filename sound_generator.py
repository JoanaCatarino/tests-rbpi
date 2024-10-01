# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:45:04 2024

@author: JoanaCatarino
"""

import sys
import numpy as np
import asyncio
from PyQt5 import QtWidgets, QtCore
import pyaudio


def generate_white_noise(duration, sample_rate=44100, amplitude=0.1):
    samples = np.random.normal(0, amplitude, int(sample_rate * duration))
    return samples

def play_sound(sound, sample_rate=44100):
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paFloat32,
                    channels = 1,
                    rate = sample_rate,
                    output = True)
    stream.write(sound.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()
    
def white_noise():
    sample_rate = 44100  # Sample rate in Hz
    duration = 2  # Duration in seconds
    sound = generate_white_noise(duration, sample_rate)
    play_sound(sound, sample_rate)

