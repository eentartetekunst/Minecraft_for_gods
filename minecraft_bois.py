import pygame, sys
from pygame.locals import *

FPS = 30 #Frames per Second parameter 
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)

class Character():
    def __init__(self, fighter, x_pos, y_pos):
        self.fighter = fighter
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def image_init(self):
        self.PLAYER_IMG = pygame.image.load(self.fighter)
        self.PLAYER_IMG = pygame.transform.scale(self.PLAYER_IMG, (300,300))
        DISPLAYSURF.blit(self.PLAYER_IMG, (self.x_pos, self.y_pos))
        
def main():
    global DISPLAYSURF
    BACKGROUND = pygame.image.load('Yyy.png')
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WINDOWWIDTH,WINDOWHEIGHT))
    DISPLAYSURF.blit(BACKGROUND,(0,0))
    PLAYER_OBJ = Character('heroes.png', 0, 0)
    
    while True:
        DISPLAYSURF.blit(BACKGROUND,(0,0))
        moveUp = False
        moveDown = False
        moveRight = False
        moveLeft = False
        #Record all events 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    moveDown = False
                    moveUp = True
                elif event.key in (K_DOWN, K_s):
                    moveUp = False
                    moveDown = True
                elif event.key in (K_LEFT, K_a):
                    moveRight = False
                    moveLeft = True
                elif event.key in (K_RIGHT, K_d):
                    moveLeft = False
                    moveRight = True
        #Update position of a player and blit
        if moveUp==True:
            PLAYER_OBJ.y_pos -= 5
        elif moveDown==True:
            PLAYER_OBJ.y_pos += 5
        elif moveRight==True:
            PLAYER_OBJ.x_pos += 5
        elif moveLeft==True:
            PLAYER_OBJ.x_pos -= 5     
        PLAYER_OBJ.image_init()
        
        pygame.display.update()
     
    
    
if __name__ == "__main__":
    main()
