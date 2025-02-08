import pygame
from constants import *
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0
    player1 = player.Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
                                
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        dt = (fps_clock.tick(60)/1000)






if __name__ == "__main__":
    main()
