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


speed=pygame.math.Vector2(0,0)


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

        global speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                main = fales

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print ('left')
                    speed[0] =(-2)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print ('right')
                    speed[0] =(2)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print ('jump')
                    speed[1] =(-2)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print ('down')
                    speed[1] =(2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                    speed[0] = (0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                    speed[0] = (0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('up stop')
                    speed[1] = (0)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down stop')
                    speed[1] = (0)

        clock.tick(60)
        movefish()
        screen.fill(color)
        screen.blit(fish_image,fish_rect)
        pygame.display .flip()

if __name__ == '__main__':
    main()

