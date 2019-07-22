import sys,pygame
from pygame. locals import *

pygame.init()
screen_info = pygame.dusplay.info()

screen = pygame.display.set_model(int(screen_info.current_w),int(screen_info.current_h))
clock = pygame.time.clock()

def main():
    while True:
        clock.tick(60)
        screen fill(0,120,200)
        pygame.display .flip()
if name = "_main_":
    main()