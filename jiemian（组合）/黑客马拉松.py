import pygame
import sys
import random
import os
import time
import math

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

global lastx
global lasty

def draw(position,k):
    pygame.draw.circle(surface,color[k],position,100,100)

def main():
    pygame.init()
    pygame.mixer.init()
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
        # if lastx >= 50 and lastx <= 150 and lasty >= 200 and lasty <= 240:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(START_ON, (50, 200))
        # elif lastx >= 200 and lastx <= 290 and lasty >= 550 and lasty <= 600:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(DRUM_ON, (200, 550))
        # elif lastx >= 310 and lastx <= 410 and lasty >= 550 and lasty <= 600:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(CRASH_ON, (310, 550))
        # elif lastx >= 430 and lastx <= 530 and lasty >= 550 and lasty <= 600:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(HITHAT_ON, (430, 550))
        # elif lastx >= 550 and lastx <= 670 and lasty >= 550 and lasty <= 600:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(RIMSHOT_ON, (550, 550))
        # elif lastx >= 720 and lastx <= 775 and lasty >= 550 and lasty <= 600:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(PF_ON, ( 720, 550))
        # elif lastx >= 800 and lastx <= 870 and lasty >= 550 and lasty <= 600:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(PSH_ON, (800, 550))
        # elif lastx >= 890 and lastx <= 1000 and lasty >= 550 and lasty <= 600:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(LIPROLL_ON, (890, 550))
        # elif lastx >= 120 and lastx <= 180 and lasty >= 550 and lasty <= 600:
        #     pygame.mouse.set_cursor(pygame.cursors.arrow)
        #     surface.blit(ZIP_ON, (120, 550))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lastx >= 50 and lastx <= 150 and lasty >= 200 and lasty <= 240:
                surface.blit(START_ON, (50, 200))
                B.play()
            elif lastx >= 200 and lastx <= 290 and lasty >= 550 and lasty <= 600:
                surface.blit(DRUM_ON,(200,550))
                DRUMV.set_volume(0.5)
                DRUMV.play()
            elif lastx >= 310 and lastx <= 410 and lasty >= 550 and lasty <= 600:
                surface.blit(CRASH_ON, (310, 550))
            elif lastx >= 430 and lastx <= 530 and lasty >= 550 and lasty <= 600:
                surface.blit(HITHAT_ON,(430,550))
                HITHATV.set_volume(0.5)
                HITHATV.play()
            elif lastx >= 550 and lastx <= 670 and lasty >= 550 and lasty <= 600:
                surface.blit(RIMSHOT_ON,(550,550))
                RIMSHOTV.set_volume(0.5)
                RIMSHOTV.play()
            elif lastx >= 720 and lastx <= 775 and lasty >= 550 and lasty <= 600:
                surface.blit(PF_ON, (720, 550))
                PFV.play()
            elif lastx >= 800 and lastx <= 870 and lasty >= 550 and lasty <= 600:
                surface.blit(PSH_ON, (800, 550))
                PSHV.play()
            elif lastx >= 890 and lastx <= 1000 and lasty >= 550 and lasty <= 600:
                surface.blit(LIPROLL_ON, (890, 550))
                LIPROLLV.play()
            elif lastx >= 120 and lastx <= 180 and lasty >= 550 and lasty <= 600:
                surface.blit(ZIP_ON, (120, 550))
                ZIPV.play()

        pygame.display.flip()
        pygame.display.update()

if __name__=='__main__':
     main()
