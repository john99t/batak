# batak
Batak-like reaction tester using hardware controlled by a Raspberry Pi

Written in Python 3 

# IOPi Input/Output Card uses I2C

Bus 1 (Address 0x20) - switches short to GND (against internal pull-up resistors)
Bus 2 (Address 0x21) - lights via relay board

# Relay board

Relays run opto-isolated 12V separate from 3.3V/5V from Raspberry Pi: http://arduinoinfo.mywikis.net/wiki/RelayIsolation

External PSU to GND & JD-VCC
IOPi: Vcc to Relay VCC & I/O pin 1 to IN1

Not necessary to connect IOPi GND to Relay GND


# LCD using I2C

Address 0x27


```
sudo pip3 install pycodestyle
pycodestyle --exclude=LICENSE,README.md *
```

