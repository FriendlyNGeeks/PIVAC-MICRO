# SPDX-FileCopyrightText: 2022 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

import _thread
from api_monitor import startMonitor
from api_server import startApi


def start_apiServer():
    startApi.start()

def start_monServer():
   startMonitor.start()

        
# Function that initializes execution in the second core
# The second argument is a list or dictionary with the arguments
# that will be passed to the function.
_thread.start_new_thread(start_apiServer, ())
_thread.start_new_thread(start_monServer, ())
