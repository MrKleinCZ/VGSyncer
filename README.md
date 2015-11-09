# VGSyncer
Small (in footprint) MIDIoverUSB controller for Roland GR-55 and GP-10. Based on RaspberryPi.
# Planned Features
* quick select required "user bank" on GR-55 by footswitches
* on "map" based on GR-55 "user bank":"patch" combination - launch desired patch on GP-10
* on bank/patch launch event change selected parametes on both devices (f.e. S1/S2 assign, Volume assign, etc.)
* LCD display GR/GP patch names, selected "map" and status: "SYNC ON", "Unchained", "MUTED", etc.

# Hardware
* RaspberryPi 2
* 20x4 LCD, 4x menu navigation buttons

# Software
* Raspbian Jessie (with some tweaks: slimmer image, reduced writes to SD card, etc.)
* Python Scripts running as "daemons" (with "python-rtmidi", "LCD" and other libraries)
