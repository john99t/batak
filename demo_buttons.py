#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drivers import buttondriver

from time import sleep

button_panel = buttondriver.ButtonPanel()

sleep(2)  # 2 sec delay

print("All lights ON!")
button_panel.button_set_all(1)

sleep(2)  # 2 sec delay
print("All lights OFF!")
button_panel.button_set_all(0)

