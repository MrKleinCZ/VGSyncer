#!/usr/bin/env python

#***************************************************************************
#*
#* Copyright (C) 2015,2016 by Jirka Maly <jirka@mrklein.cz>
#* All rights reserved.
#* This file is part of "VGSyncer" software.
#*
#* This program is free software; you can redistribute it and/or modify
#* it under the terms of the GNU General Public License as published by
#* the Free Software Foundation; either version 2 of the License, or
#* (at your option) any later version.
#*
#* This program is distributed in the hope that it will be useful,
#* but WITHOUT ANY WARRANTY; without even the implied warranty of
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#* GNU General Public License for more details.
#*
#* You should have received a copy of the GNU General Public License along
#* with this program; if not, write to the Free Software Foundation, Inc.,
#* 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#*
#**************************************************************************

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
