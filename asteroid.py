import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(split_angle) * ASTEROID_SPLIT_SPEED_UP

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = self.velocity.rotate(-split_angle) * ASTEROID_SPLIT_SPEED_UP
        
