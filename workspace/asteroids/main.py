# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, update_group, draw_group)
    AsteroidField.containers = (update_group,)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, update_group, draw_group)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.get_time() / 1000

        update_group.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                return      
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for sprite in draw_group:
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
