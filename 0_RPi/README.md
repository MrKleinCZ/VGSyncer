#RPi
after some cleaning I'm actually on 900MB of used space and ~380MB compressed image size.
There is alredy Apache2 with PHP for possible web based config and controll. 

#Python Libraries
Download source "zip" or "tar.gz". Libraries containing C/C++ code must be compilled for ARM processors on Raspberry.
* [Cython](https://pypi.python.org/pypi/Cython) - required to build "python-rtmidi"
* [python-rtmidi](https://pypi.python.org/pypi/python-rtmidi) - MIDI client (creates, read, write to MIDI client)
* [Adafruit_Python_CharLCD] (https://github.com/adafruit/Adafruit_Python_CharLCD) - RaspberryPi LCD Driver library
* [Adafruit_Python_GPIO] (https://github.com/adafruit/Adafruit_Python_GPIO) - RaspberryPi I2C (MCP23017) Driver library
* [pyOSC] (https://pypi.python.org/pypi/pyOSC) - OSC server and client for future OSC support. 
