import sys,pygame

# from pygame. locals import *
pygame.init()
screen_info = pygame.display.Info()
# set the width and height to the size of screen
size = (width, height) = ((int(screen_info.current_w), int(screen_info.current_h)))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (110, 170, 255)

fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.smoothscale(fish_image,(280, 160))

fish_rect = fish_image.get_rect()


fish_rect.center = (width//2, height//2)

rotation = random.randint(0,360)
speed.rotate_ip(rotation)


fish_image = pygame.transform.rotate(fish_image, 180 - rotation)


speed=pygame.math.Vector2(15,10)

def movefish():
    global color
    global fish_image
    size = (width, hight) = (int(screen_info.current_w), int(screen_info.current_h))
    fish_rect.move_ip(speed)

    fish_rect.left < 0
    fish_rect.right
    fish_rect.top

    if fish_rect.bottom > height:
        speed[1] *= -1
        color = (255,125, 20)
    if fish_rect.top < (0):
        speed[1] *= -1
        color = (255, 120, 120)
    if fish_rect.right > width:
        speed[0] *= -1
        color = (0,255, 120)
        fish_image = pygame.transform.flip(fish_image, True, False)
    if fish_rect.left < (0):
        speed[0] *= -1
        color = (110, 170, 255)
        fish_image = pygame.transform.flip(fish_image, True, False)
def main():
    while True:
        clock.tick(60)
        movefish()
        screen.fill(color)
        screen.blit(fish_image,fish_rect)
        pygame.display .flip()


if __name__ == '__main__':
    main()

