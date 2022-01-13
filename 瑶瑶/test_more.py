import subprocess
import keyboard  # Using module keyboard
import pygame
import time
#
# pygame.init()
#
# while True:#making a loop
#     do = subprocess.Popen(['aplay', 'out'])
#     try: #used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('0'):#if key 'q' is pressed
#             print('You Pressed 0!')
#             break#finishing the loop
#         else:
#             pass
#     except:
#         do = subprocess.Popen(['aplay', 'out1'])
#         try:
#             if keyboard.is_pressed('1'):#if key 'q' is pressed
#                 print('You Pressed 1!')
#                 break#finishing the loop
#             else:
#                 pass
#         except:
#             break #if user pressed other than the given key the loop will break

pygame.init()

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


# import keyboard  # Using module keyboard
# import pygame
# import time
# import subprocess
# pygame.init()
# import keyboard #Using module keyboard
# while True:
#     if keyboard.is_pressed('w'):
#         while True:
#             do = subprocess.Popen(['aplay', 'out'])
#             time.sleep(0.5)
#             if keyboard.is_pressed('q'):
#                 break
#     elif keyboard.is_pressed('r'):
#         while True:
#             re = subprocess.Popen(['aplay', 'out2'])
#             if keyboard.is_pressed('e'):
#                 break