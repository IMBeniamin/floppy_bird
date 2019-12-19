import pygame
# from random import randint
colors = {'white': (0, 0, 0),
          'red': (255, 0, 0),
          'green': (0, 255, 0),
          'yellow': (255, 255, 0),
          'magenta': (255, 0, 255),
          'cyan': (0, 255, 255),
          'pink': (255, 125, 255),
          'blue': (0, 0, 255),
          'black': (255, 255, 255)
          }
ch = 700
cl = 1200
posX = 10
posY = 10
velX = velY = 1

pygame.init()
screen = pygame.display.set_mode((cl, ch))
clock = pygame.time.Clock()

floppy_bird_srf = pygame.image.load('media/bird.png').convert()
floppy_bird_srf = pygame.transform.scale(floppy_bird_srf, (100, 75))
floppy_bird = floppy_bird_srf.get_rect()
floppy_bird.center = (350, 300)
screen.blit(floppy_bird_srf, floppy_bird)


def mainloop():
    """Main loop of the game
    """
    global posX, posY, floppy_bird, floppy_bird_srf

    done = False
    while not done:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.event.pump()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            floppy_bird = floppy_bird.move((0, -10))
        if pressed[pygame.K_q]:
            done = True
        else:
            floppy_bird = floppy_bird.move((0, 5))
        '''
        else:
            posY += 1
        '''

        screen.blit(floppy_bird_srf, floppy_bird)
        # pygame.draw.rect(screen, colors['blue'], pygame.Rect(posX, posY, 50, 50))

        clock.tick(60)
        pygame.display.flip()


mainloop()
