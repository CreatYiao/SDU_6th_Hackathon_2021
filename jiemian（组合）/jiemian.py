import pygame
import keyboard
import time
import main
import subprocess
surface = pygame.display.set_mode((1200,640))
white = (255, 255, 255)
black = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,128)
color=[white,BLUE,black,GREEN]
background = pygame.image.load('背景.png').convert_alpha()
START = pygame.image.load('START.png').convert_alpha()
START_ON = pygame.image.load('START_ON.png').convert_alpha()
DRUM = pygame.image.load('DRUM.png').convert_alpha()
DRUM_ON = pygame.image.load('DRUM_ON.png').convert_alpha()
CRASH = pygame.image.load('CRASH.png').convert_alpha()
CRASH_ON = pygame.image.load('CRASH_ON.png').convert_alpha()
RIMSHOT = pygame.image.load('RIMSHOT.png').convert_alpha()
RIMSHOT_ON = pygame.image.load('RIMSHOT_ON.png').convert_alpha()
ZIP = pygame.image.load('ZIP.png').convert_alpha()
ZIP_ON = pygame.image.load('ZIP_ON.png').convert_alpha()
HITHAT = pygame.image.load('HITHAT.png').convert_alpha()
HITHAT_ON = pygame.image.load('HITHAT_ON.png').convert_alpha()
LIPROLL = pygame.image.load('LIPROLL.png').convert_alpha()
LIPROLL_ON = pygame.image.load('LIPROLL_ON.png').convert_alpha()
PSH = pygame.image.load('PSH.png').convert_alpha()
PSH_ON = pygame.image.load('PSH_ON.png').convert_alpha()
PF = pygame.image.load('PF.png').convert_alpha()
PF_ON = pygame.image.load('PF_ON.png').convert_alpha()
li = []
global lastx
global lasty

def draw(position,k):
    pygame.draw.circle(surface,color[k],position,100,100)

def main1():
    pygame.init()
    pygame.mixer.init()
    DRUMV = pygame.mixer.Sound('drum.wav')
    HITHATV = pygame.mixer.Sound('hithat.wav')
    RIMSHOTV = pygame.mixer.Sound('rimshot.wav')
    PFV = pygame.mixer.Sound('pf.wav')
    PSHV = pygame.mixer.Sound('psh.wav')
    LIPROLLV = pygame.mixer.Sound('liproll.wav')
    ZIPV = pygame.mixer.Sound('zip.wav')
    B = pygame.mixer.Sound('b.wav')
    pygame.display.set_mode((1200,640))
    b1 = 2
    b2 = 2
    b3 = 2
    while(1):
        surface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        x, y = pygame.mouse.get_pos()
        lastx = x
        lasty = y
        pygame.mouse.set_cursor(pygame.cursors.tri_left)
        surface.blit(START, (50, 200))
        surface.blit(ZIP, (120, 550))
        surface.blit(DRUM, (200, 550))
        surface.blit(CRASH, (310, 550))
        surface.blit(HITHAT, (430, 550))
        surface.blit(RIMSHOT, (550, 550))
        surface.blit(PF, (720, 550))
        surface.blit(PSH, (800, 550))
        surface.blit(LIPROLL, (890, 550))
        if keyboard.is_pressed('0'):
                surface.blit(START_ON, (50, 200))
                do = subprocess.Popen(['aplay', 'out'])
                li.append('out')
                time.sleep(0.5)
        elif keyboard.is_pressed('1'):
            surface.blit(DRUM_ON,(200,550))
            re = subprocess.Popen(['aplay', 'out1'])
            li.append('out1')
            time.sleep(0.5)
        elif keyboard.is_pressed('2'):
            surface.blit(CRASH_ON, (310, 550))
            mi = subprocess.Popen(['aplay', 'out2'])
            li.append('out2')
            time.sleep(0.5)
        elif keyboard.is_pressed('3'):
            surface.blit(HITHAT_ON,(430,550))
            fa = subprocess.Popen(['aplay', 'ou3'])
            li.append('out3')
            time.sleep(0.5)
        elif keyboard.is_pressed('4'):
            surface.blit(RIMSHOT_ON,(550,550))
            so = subprocess.Popen(['aplay', 'out4'])
            li.append('out4')
            time.sleep(0.5)
        elif keyboard.is_pressed('5'):
            surface.blit(PF_ON, (720, 550))
            la = subprocess.Popen(['aplay', 'out5'])
            li.append('out5')
            time.sleep(0.5)
        elif keyboard.is_pressed('6'):
            surface.blit(PSH_ON, (800, 550))
            xi = subprocess.Popen(['aplay', 'out6'])
            li.append('out6')
            time.sleep(0.5)
        elif keyboard.is_pressed('7'):
            surface.blit(LIPROLL_ON, (890, 550))
            re_ = subprocess.Popen(['aplay', 'out7'])
            li.append('out7')
            time.sleep(0.5)
        elif keyboard.is_pressed('8'):
            surface.blit(ZIP_ON, (120, 550))
            do_ = subprocess.Popen(['aplay', 'out8'])
            li.append('out8')
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
        elif keyboard.is_pressed('x'):
            for music in li:
                time.sleep(0.3)
                subprocess.Popen(['aplay', music])
        elif keyboard.is_pressed('c'):
            for i in range(1):
                print('clear successful!')
                li.clear()
        
        pygame.display.flip()
        pygame.display.update()

if __name__=='__main__':
     main1()
