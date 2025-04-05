from itertools import cycle
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def traffic_light_simulation():
    tl_config = [
        ('🔴', 2),
        ('🟢', 2),
        ('🟡', 1),
    ]
    
    state = cycle(tl_config) 
    
    try:
        while True:
            color, duration = next(state)
            clear_screen()
            print(f"Traffic light is: {color}")
            time.sleep(duration)
    except KeyboardInterrupt:
        clear_screen()
        print("Simulation stopped.")

traffic_light_simulation()
