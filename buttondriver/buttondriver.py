# -*- coding: utf-8 -*-
"""
Driver for Raspbery Pi illuminated buttons
"""


class buttons:

    # initializes button state
    def __init__(self):
        pass

    def button_read(self, id):
        """
        read the value of an individual button 1 - 16
        returns 0 = logic level low, 1 = logic level high
        """
        return 0

    def button_write(self, id, value):
        """
        sets the illumination value of an individual button 1 - 16
        value will be 0 = unlit, 1 = illuminated
        """
        pass
