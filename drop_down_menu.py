# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:19:13 2024

@author: JoanaCatarino
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
from PyQt5.QtGui import QFont  # Import QFont for font manipulation

def animal_id(combobox, font_size=10):
    items = ["Test-animal", "52345", "53455", "12846", "12364", "34456"]
     
    # Create a font with the specified size
    font = QFont()
    font.setPointSize(font_size)
     
    # Apply the font to the combo box
    combobox.setFont(font)
     
    for item in items:
        combobox.addItem(item)
         
         
         