#!/usr/bin/python

"""
This is just test if all libraries are working and can connect to synths
"""
 
#import
import rtmidi as rtmidi
import time

def callback_midi(message, user_data):
    print message[0][0:18],'.....'    
    if message[0][0:3] == [0xF0, 0x41, 0x10]:
      sysexdata=''
      for sybytes in message[0][12:24]:
        sysexdata+=chr(sybytes)
      print sysexdata
 
def main():
  # Main program block
  midi_in = rtmidi.MidiIn(2,"VGSync",100)
  print 'Available MIDI IN:', midi_in.get_ports()
  midi_in.open_port(1,"VGSync In1")
  midi_in.set_callback(callback_midi)
  midi_in.ignore_types (False, False, False )
  
  midi_out = rtmidi.MidiOut(2,"VGSync")
  midi_out.open_port(1,"VGSync Out1")

  time.sleep(2) # 2 second delay
  
  midi_out.send_message([0xF0, 0x7E, 0x10, 0x06, 0x01, 0xF7])

  
  while True:
    
    
    midi_out.send_message([0xF0, 0x41, 0x10, 0x00, 0x00, 0x00, 0x05, 0x11, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x54, 0xF7])
  
    time.sleep(2) # 2 second delay
   
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print 'bye!'
    

