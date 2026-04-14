#!/usr/bin/env python3
from gpiozero import Button
from signal import pause

# Set up the sensor on GPIO 17 (physical pin 11)
# The pull_up parameter is set to False because the LM393 module will output a clear HIGH signal.
water_sensor = Button(17, pull_up=False)

def water_detected():
    print("💧 WATER DETECTED!")

def no_water():
    print("✅ No water detected")

# Assign the functions to the button's events
water_sensor.when_pressed = water_detected
water_sensor.when_released = no_water

print("Water detector ready. Waiting for sensor events...")
pause()