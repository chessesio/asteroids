import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (all_shots, updatable, drawable)

    player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for an_asteroid in all_asteroids:
            if an_asteroid.check_collision(player1):
                raise SystemExit("Game Over. Player Collision")
            for a_shot in all_shots:
                if a_shot.check_collision(an_asteroid):
                    raise SystemExit("Game Over. Shot Collision")
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        for shot in all_shots:
            shot.draw(screen)
        pygame.display.flip()
        dt = (fps_clock.tick(60)/1000)






if __name__ == "__main__":
    main()
