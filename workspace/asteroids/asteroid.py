import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity = self.velocity * 1.2
        if new_radius < ASTEROID_MIN_RADIUS:
            self.kill()
            return
        random_angle = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity.rotate(random_angle)
        asteroid2.velocity = new_velocity.rotate(-random_angle)

        for group in self.groups():
            group.add(asteroid1)
            group.add(asteroid2)

        self.kill()
