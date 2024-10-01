# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:02:38 2024

@author: JoanaCatarino
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from form import Ui_Widget

from diff_functions import Functions
from gpio_map import *

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    # Initialize the different controls in the gui    
    self.controls = Functions(self.ui)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
