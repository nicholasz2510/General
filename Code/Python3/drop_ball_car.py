import math
import time
from playsound import playsound

h = float(input("What is the height from which the ball will be dropped? (in m) "))
d = float(input("What is the distance between the car and the spot where the ball will hit? (in cm) "))
s = float(input("What is the speed of the car? (in cm/s) "))

wait_time = (d / s) - (math.sqrt((2 * d) / 9.80665))

input("Let the car go and press Enter at the same time")
print("\nWait...")

if wait_time >= 1.5:
    time.sleep(wait_time - 1.0)
    print("\nDrop on the third beat!")
    playsound("ready_set_go.wav")
else:
    print("\nDrop when you hear the beat!")
    time.sleep(wait_time)
    playsound("go2.wav")
