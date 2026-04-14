#!/usr/bin/env python3
from gpiozero import Button
from signal import pause


water_sensor = Button(17, pull_up=False)

def water_detected():
    print("💧 WATER DETECTED!")

def no_water():
    print("✅ No water detected")


water_sensor.when_pressed = water_detected
water_sensor.when_released = no_water

print("Water detector ready. Waiting for sensor events...")
pause()
