# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:09:13 2024

@author: JoanaCatarino
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from form import Ui_Widget

from drop_down_menu import animal_id
from led import blueLED
from sound_generator import white_noise

class Functions:
    
    def __init__(self, ui):
        self.ui = ui
        
        # initialize components:
        self.populate_dropdown()
        self.ui.QRadioButton.clicked.connect(self.blueLED())
        self.ui.QCheckBox.clicked.connect(self.white_noise())
        self.ui.QPushButton.clicked.connect(self.press())
        
    def populate_dropdown(self):
        # Populate the dropdown menu for Animal_ID
        font_size = 10  # Font size of the items in the dropdown menu
        animal_id(self.ui.QComboBox)    
            
    def press(self):
        print('Pressed!')        