import sys,pygame
from pygame. locals import *

pygame.init()
screen_info = pygame.display.Info()

screen = pygame.display.set_mode((int(screen_info.current_w), int(screen_info.current_h)))
clock = pygame.time.Clock()
color = (200, 0, 200)

fish_image = pygame.image.load("fish.png")

fish_rect = fish_image.get_ret()

def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        pygame.display .flip()


if __name__ == '__main__':
    main()

