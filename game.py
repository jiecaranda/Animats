import pygame
from pygame.locals import *

import environment
import cell

def draw(screen, env):
    for i in range(env.width):
        for j in range(env.height):
            drawCell(screen, env.grids[i][j], i, j)

    for i in range(len(env.foods)):
        drawCell(screen, env.foods[i], env.foods[i].x, env.foods[i].y)

    for i in range(len(env.nonfoods)):
        drawCell(screen, env.nonfoods[i], env.nonfoods[i].x, env.nonfoods[i].y)

    for i in range(len(env.animats)):
        drawCell(screen, env.animats[i], env.animats[i].x, env.animats[i].y)

def drawCell(screen, cell, i, j):
    sx = i*cell.Size
    sy = j*cell.Size
    screen.fill(cell.color, (sx, sy, cell.Size, cell.Size))


# Initialize the game
pygame.init()

width, height = 800, 800
screen=pygame.display.set_mode((width, height))


env = environment.Environment(width / cell.Cell.Size, height / cell.Cell.Size)
env.createFoods(20)
env.createNonFoods(20)
env.createAnimats()
 
# keep looping through
while 1:
    #  clear the screen before drawing it again
    screen.fill(0)
    #  draw the screen elements
    env.update()
    draw(screen, env)
    #  update the screen
    pygame.display.flip()
    # loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)