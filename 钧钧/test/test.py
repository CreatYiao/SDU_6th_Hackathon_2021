import keyboard  # Using module keyboard
import pygame
import time
import subprocess
import main

pygame.init()
import keyboard  # Using module keyboard
li = []
while True:
    if keyboard.is_pressed('0'):
        while True:
            if keyboard.is_pressed('1'):
                do = subprocess.Popen(['aplay', 'out'])
                li.append('out')
                time.sleep(0.5)
            elif keyboard.is_pressed('2'):
                re = subprocess.Popen(['aplay', 'out2'])
                li.append('out2')
                time.sleep(0.5)
            elif keyboard.is_pressed('3'):
                mi = subprocess.Popen(['aplay', 'out3'])
                li.append('out3')
                time.sleep(0.5)
            elif keyboard.is_pressed('4'):
                fa = subprocess.Popen(['aplay', 'out4'])
                li.append('out4')
                time.sleep(0.5)
            elif keyboard.is_pressed('5'):
                so = subprocess.Popen(['aplay', 'out5'])
                li.append('out5')
                time.sleep(0.5)
            elif keyboard.is_pressed('6'):
                la = subprocess.Popen(['aplay', 'out6'])
                li.append('out6')
                time.sleep(0.5)
            elif keyboard.is_pressed('7'):
                xi = subprocess.Popen(['aplay', 'out7'])
                li.append('out7')
                time.sleep(0.5)
            elif keyboard.is_pressed('8'):
                do_ = subprocess.Popen(['aplay', 'out8'])
                li.append('out8')
                time.sleep(0.5)
            elif keyboard.is_pressed('9'):
                re_ = subprocess.Popen(['aplay', 'out9'])
                li.append('out9')
                time.sleep(0.5)
            elif keyboard.is_pressed('q'):
                main.record_audio('out', 1.5)
            elif keyboard.is_pressed('w'):
                main.record_audio('out2', 1.5)
            elif keyboard.is_pressed('e'):
                main.record_audio('out3', 1.5)
            elif keyboard.is_pressed('r'):
                main.record_audio('out4', 1.5)
            elif keyboard.is_pressed('t'):
                main.record_audio('out5', 1.5)
            elif keyboard.is_pressed('y'):
                main.record_audio('out6', 1.5)
            elif keyboard.is_pressed('u'):
                main.record_audio('out7', 1.5)
            elif keyboard.is_pressed('i'):
                main.record_audio('out8', 1.5)
            elif keyboard.is_pressed('o'):
                main.record_audio('out9', 1.5)
            elif keyboard.is_pressed('z'):
                print('exit')
                break
    elif keyboard.is_pressed('x'):
        for music in li:
            time.sleep(0.3)
            subprocess.Popen(['aplay', music])
    elif keyboard.is_pressed('c'):
        for i in range(1):
            print('clear successful!')
            li.clear()

s
