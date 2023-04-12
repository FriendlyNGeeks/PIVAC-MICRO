import time
from machine import Pin
from neopixel import NeoPixel


power_pin = Pin(21, Pin.OUT)  # NeoPixel power is on pin 21
power_pin.on()  # Enable the NeoPixel Power

pin = Pin(33, Pin.OUT)  # Onboard NeoPixel is on pin 33
np = NeoPixel(pin, 1)  # create NeoPixel driver on pin 33 for 1 pixel

led = Pin(13, Pin.OUT)
btn1Pin = Pin(1, Pin.IN)


class startMonitor():
    def start():
        while True:
            logic_state = btn1Pin.value()
            if logic_state == True:     # if pressed the push_button
                led.value(1)             # led will turn ON
            else:                       # if push_button not pressed
                led.value(0)             # led will turn OFF
            np.fill((0, 155, 0))  # Set the NeoPixel blue
            np.write()  # Write data to the NeoPixel
            time.sleep(0.5)  # Pause for 0.5 seconds
            np.fill((0, 0, 0))  # Turn the NeoPixel off
            np.write()  # Write data to the NeoPixel
            time.sleep(0.5)  # Pause for 0.5 seconds
