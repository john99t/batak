# -*- coding: utf-8 -*-
"""
Driver for Raspbery Pi illuminated buttons
"""
from drivers.IOPi import IOPi

# Bus 1 (buttons) I2C address
BUS1_ADDRESS = 0x20

# Bus 2 (lights) I2C address
BUS2_ADDRESS = 0x21


class ButtonPanel:

    # initializes button state
    def __init__(self):
        self.buttons = IOPi(BUS1_ADDRESS)
        self.buttons.set_port_direction(0, 0xFF) # 1 = input, 0 = output
        self.buttons.set_port_direction(1, 0xFF) # 1 = input, 0 = output
        self.buttons.invert_port(0, 0xFF)        # make button pressed = 1
        self.buttons.invert_port(1, 0xFF)        # make button pressed = 1
        self.buttons.set_port_pullups(0, 0xFF)   # pullup enabled
        self.buttons.set_port_pullups(1, 0xFF)   # pullup enabled
        self.lights = IOPi(BUS2_ADDRESS)
        self.lights.set_port_direction(0, 0x00)  # 1 = input, 0 = output
        self.lights.set_port_direction(1, 0x00)  # 1 = input, 0 = output
        self.lights.write_port(0, 0xFF)
        self.lights.write_port(1, 0xFF)

    def button_read(self, id):
        """
        read the value of an individual button 1 - 16
        returns 0 = open, 1 = closed
        """
        return self.buttons.read_pin(id)

    def button_write(self, id, value):
        """
        sets the illumination value of an individual button 1 - 16
        value will be 0 = unlit, 1 = illuminated
        """
        self.lights.write_pin(id, value)
