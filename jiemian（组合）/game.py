import pygame
import sys
import random
import os
import time
surface = pygame.display.set_mode((600,600))
food_pos = [random.randrange(1, 59) * 10, random.randrange(1, 59) * 10]
white = (255, 255, 255)
black = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,128)
snake_pos = [[300, 300], [290, 300], [280, 300], [270, 300]]
head_pos = [300, 300]
global last_key
global game
clock = pygame.time.Clock()

class snakeking:
    def __init__(self,head_pos,snake_pos):
        self.snake_pos = snake_pos
        self.head_pos = head_pos
        self.last_key = pygame.K_RIGHT

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.last_key != pygame.K_RIGHT:
                    self.last_key = pygame.K_LEFT
                    self.head_pos[0] -= 10
                elif event.key == pygame.K_RIGHT and self.last_key != pygame.K_LEFT:
                    self.last_key = pygame.K_RIGHT
                    self.head_pos[0] += 10
                elif event.key == pygame.K_DOWN and self.last_key != pygame.K_UP:
                    self.last_key = pygame.K_DOWN
                    self.head_pos[1] += 10
                elif event.key == pygame.K_UP and self.last_key != pygame.K_DOWN:
                    self.last_key = pygame.K_UP
                    self.head_pos[1] -= 10
                self.snake_pos.insert(0, list(self.head_pos))
                self.snake_pos.pop()
        if True:
            if self.last_key == pygame.K_LEFT:
                self.head_pos[0] -= 10
            elif self.last_key == pygame.K_RIGHT:
                self.head_pos[0] += 10
            elif self.last_key == pygame.K_DOWN:
                self.head_pos[1] += 10
            elif self.last_key == pygame.K_UP:
                self.head_pos[1] -= 10
            self.snake_pos.insert(0, list(self.head_pos))
            self.snake_pos.pop()
    def display(self):
        for pos in self.snake_pos:
            draw1(pos)
        pygame.display.update()

    def judge(self,food_pos,game):
        for i in range(2, len(self.snake_pos)):
            if self.head_pos == self.snake_pos[i] or self.head_pos[0] < 0 or self.head_pos[0] > 600 or self.head_pos[1] < 0 or self.head_pos[1] > 600:
                font = pygame.font.SysFont('Times', 30)
                text = font.render('GAME OVER!', True, (0, 0, 255), (0, 255, 0))
                surface.blit(text, (230, 250))
                pygame.display.flip()
                time.sleep(0.8)
                game = False
            else:
                game = True
                return game

def menu(snake):
    font = pygame.font.SysFont('Times', 30)
    text = font.render('RESTART', True, (0, 0, 255), (0, 255, 0))
    surface.blit(text, (180, 250))
    text = font.render('EXIT', True, (0, 0, 255), (0, 255, 0))
    surface.blit(text, (400, 250))
    pygame.display.flip()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                if x>=180 and x<=320 and y>=250 and y<=280 or x>=400 and x<=470 and y>=250 and y<=280:
                    pygame.mouse.set_cursor(pygame.cursors.diamond)
                else:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x>=180 and x<=320 and y>=250 and y<=280:
                    main()
                elif x>=400 and x<=470 and y>=250 and y<=280:
                    pygame.quit()
                    exit()

def draw(position):
    pygame.draw.rect(surface,white,pygame.Rect(position[0],position[1],10,10))
def draw1(position):
    pygame.draw.rect(surface,GREEN,pygame.Rect(position[0],position[1],10,10))

def eat(snake,food_pos,score):
    if snake.head_pos == food_pos or snake.snake_pos[1] == food_pos:
        snake.snake_pos.insert(0, list(snake.head_pos))
        score += 1
        return [random.randrange(1, 59) * 10, random.randrange(1, 59) * 10],score
    else:
        return food_pos,score
def main():
    pygame.init()
    snake_pos = [[300, 300], [290, 300], [280, 300], [270, 300]]
    head_pos = [300, 300]
    snake = snakeking(head_pos,snake_pos)
    pygame.display.set_caption("贪吃蛇")
    pygame.display.set_mode((600,600))
    global food_pos
    food_pos = [random.randrange(1, 59) * 10, random.randrange(1, 59) * 10]
    global score
    score = 0
    game = True
    pygame.display.flip()
    snake.display()
    draw(food_pos)
    pygame.display.update()
    while game :
        clock.tick(10)
        snake.move()
        food_pos,score = eat(snake,food_pos,score)
        game = snake.judge(food_pos,game)
        surface.fill(black)
        snake.display()
        draw(food_pos)
        font = pygame.font.SysFont('Times', 30)
        text = font.render('SCORE : %d' % score,True,  (0, 200, 200),(255, 255, 255))
        surface.blit(text, (450, 0))
        pygame.display.flip()
        pygame.display.update()
    surface.fill(black)
    menu(snake)

if __name__=='__main__':
     main()


