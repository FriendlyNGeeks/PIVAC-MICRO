# This file is executed on every boot (including wake-boot from deepsleep)
# Complete project details at https://RandomNerdTutorials.com

# Disable esp debug messages
import esp
esp.osdebug(None)
# Garbage collection for memory
import gc
gc.collect()
#
#import webrepl
#import webrepl_setup
#webrepl.start()
# Auto Connect to AP
import ConnectWiFi
ConnectWiFi.connect()
