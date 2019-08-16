import random
import sys
import pygame, sys
from pygame.locals import *

rectang = []

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((800,600),0,32)



    DISPLAY.fill((211,211,211))

                 
    for i in range(random.randint(3,5000)):
        WHITE=(random.randint(0,254),random.randint(0,254),random.randint(0,254))
        GREY = (random.randint(0,254),random.randint(0,254),random.randint(0,254))
        BLUE=(random.randint(0,254),random.randint(0,254),random.randint(0,254))
        pygame.draw.rect(DISPLAY,BLUE,(random.randint(0,550),i,random.randint(0,500),random.randint(0,100)))            
        pygame.draw.rect(DISPLAY,WHITE,(i,random.randint(0,550),random.randint(0,500),random.randint(0,100)))
        pygame.draw.rect(DISPLAY,WHITE,(i,i,random.randint(0,500),random.randint(0,100)))
        #pygame.draw.rect(DISPLAY,WHITE,(i,j,50,50))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
