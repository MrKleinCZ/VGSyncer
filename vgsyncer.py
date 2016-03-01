#!/usr/bin/env python

import signal, time, sys

class HandsomeKiller:
  kill_me_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_trigger)
    signal.signal(signal.SIGTERM, self.exit_trigger)
  def exit_trigger(self,signum, frame):
    self.kill_me_now = True

## Setup 1 ##




if __name__ == '__main__':
  killer = HandsomeKiller()
  ## Setup 2 ##

  while True:
    ## Mainloop ##
    
    
    time.sleep(0.01)
    if killer.kill_me_now:
      break

  ## Cleanup ##
  time.sleep(0.01)
