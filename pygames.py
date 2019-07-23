import sys,pygame
from pygame. locals import *

pygame.init()
screen_info = pygame.dusplay.info()

screen = pygame.display.set_model(int(screen_info.current_w),int(screen_info.current_h))
clock = pygame.time.clock()

def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        pygame.display .flip()
if __name__ == '__main__':
    main()

