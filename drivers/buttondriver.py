# -*- coding: utf-8 -*-
"""
Driver for Raspbery Pi illuminated buttons
"""
from drivers.IOPi import IOPi

# Bus 1 (buttons) I2C address
BUS1_ADDRESS = 0x20

# Bus 2 (lights) I2C address
BUS2_ADDRESS = 0x21

# Identifiers for each 8 line I/O port (two ports per bus)
PORT0 = 0
PORT1 = 1


class ButtonPanel:

    # initializes button state
    def __init__(self):
        # Bus 1 - input buttons
        self.buttons = IOPi(BUS1_ADDRESS)
        self.buttons.set_port_direction(PORT0, 0xFF)  # 1 = input, 0 = output
        self.buttons.set_port_direction(PORT1, 0xFF)  # 1 = input, 0 = output
        self.buttons.invert_port(PORT0, 0xFF)         # make button pressed = 1
        self.buttons.invert_port(PORT1, 0xFF)         # make button pressed = 1
        self.buttons.set_port_pullups(PORT0, 0xFF)    # pullup enabled
        self.buttons.set_port_pullups(PORT1, 0xFF)    # pullup enabled

        # Bus 2 - output lights
        self.lights = IOPi(BUS2_ADDRESS)
        self.lights.set_port_direction(PORT0, 0x00)   # 1 = input, 0 = output
        self.lights.set_port_direction(PORT1, 0x00)   # 1 = input, 0 = output
        self.lights.write_port(PORT0, 0xFF)           # 0xFF = off
        self.lights.write_port(PORT1, 0xFF)           # 0xFF = off

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
        self.lights.write_pin(id, 0 if value else 1)

    def button_write_all(self, value):
        """
        sets the illumination value of multiple buttons
        value will be between 0x0000 and 0xFFFF
        where each bit is 0 = unlit, 1 = illuminated
        """
        self.lights.write_port(PORT0, value & 0xFF)
        self.lights.write_port(PORT1, value >> 8)

    def button_set_all(self, value):
        """
        sets the illumination value of all buttons to the specified state
        value will be 0 = unlit, 1 = illuminated
        """
        self.lights.write_port(PORT0, 0x00 if value else 0xFF)
        self.lights.write_port(PORT1, 0x00 if value else 0xFF)
