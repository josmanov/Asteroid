import pygame
import constants 
from logger import log_state
from player import Player
import circleshape

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting game...")
                return
        log_state()
        screen.fill("black", None, 0)
        player.draw(screen)
        pygame.display.flip()
        clock = pygame.time.Clock()
        dt = 0
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
