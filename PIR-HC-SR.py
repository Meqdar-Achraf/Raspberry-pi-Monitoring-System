from gpiozero import MotionSensor
from time import sleep

# HC-SR501 on GPIO 17
pir = MotionSensor(17, queue_len=1)  # queue_len reduces false triggers

print("HC-SR501 PIR Sensor Test (CTRL+C to exit)")
print("Waiting 10 seconds for sensor to stabilize...")
sleep(10)  # Critical: HC-SR501 needs ~10-30 sec after power-up
print("Ready - monitoring for motion")

try:
    while True:
        pir.wait_for_motion()
        print("🚨 MOTION DETECTED!")
        pir.wait_for_no_motion()
        print("Area clear, monitoring...")
except KeyboardInterrupt:
    print("\nExiting")