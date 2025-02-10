import keyboard
import mouse
import time

print ("Press Z to START or END the clicks")

is_clicking = False

def set_clicker():
    global is_clicking
    if is_clicking:
        is_clicking = False
        print('Off')
    else:
        is_clicking = True
        print('On')
keyboard.add_hotkey('Z', set_clicker)

while True:
    if is_clicking:
        mouse.double_click(button = 'left')
        time.sleep(0.001)
    
