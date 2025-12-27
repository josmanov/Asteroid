import pygame
import constants 
from logger import log_state


def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting game...")
                return
        log_state()
        screen.fill("black", None, 0)
        pygame.display.flip()

if __name__ == "__main__":
    main()
