import pygame
from pygame.locals import * # store value to pygame locals
import sys
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((600,600))
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Chess AI")

toggle = True
each_height = 75
each_width = 75
# Draw chess board
def draw_board():
    for i in range(0, 8):

        for j in range(0, 8):
            if toggle:
                pygame.draw.rect(DISPLAYSURF, WHITE,  (j*each_width,i*each_height, each_width,each_height))
                toggle = not toggle
            else:
                pygame.draw.rect(DISPLAYSURF,BLACK,   (j*each_width,i*each_height, each_width,each_height) )
                toggle = not toggle  
        toggle = not toggle
    return


while True:
    # codes here

    pygame.display.update()
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSec.tick(FPS)