import keyboard  # Using module keyboard
import pygame
import time
import subprocess
pygame.init()
import keyboard #Using module keyboard

while True:
    if keyboard.is_pressed('w'):
        while True:
            drum = subprocess.Popen(['aplay', 'out'])
            # print(1)

            if keyboard.is_pressed('q'):
                break
            time.sleep(5)
    elif keyboard.is_pressed('r'):
        while True:
            rimshot = subprocess.Popen(['aplay', 'out1'])
            # print(2)

            if keyboard.is_pressed('e'):
                break
            time.sleep(5)