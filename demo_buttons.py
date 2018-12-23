#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drivers import buttondriver
from time import sleep

button_panel = buttondriver.ButtonPanel()

# Test all lights
print("All lights ON!")
button_panel.button_set_all(1)
sleep(2)
print("All lights OFF!")
button_panel.button_set_all(0)
sleep(2)

# Rotate light round available buttons
for i in range(10):
    for id in range(1, 6):
        button_panel.button_write(id, 1)
        sleep(0.15)
        button_panel.button_write(id, 0)

# Ensure all lights are off
button_panel.button_set_all(0)
