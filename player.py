import pygame
from enum import Enum

from constants import *
from circleshape import CircleShape
from shot import Shot

class Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 2
    RIGHT = 3

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def move(self, dt, moveDirection):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        delta = forward * PLAYER_SPEED * dt
        if (moveDirection == Direction.FORWARD):
            self.position += delta
        if (moveDirection == Direction.BACKWARD):
            self.position -= delta

    def rotate(self, dt, rotateDirection):
        if (rotateDirection == Direction.LEFT):
            self.rotation -= PLAYER_TURN_SPEED * dt
        elif (rotateDirection == Direction.RIGHT):
            self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.timer -= dt

        # movement
        if keys[pygame.K_w]:
            self.move(dt, Direction.FORWARD)
        if keys[pygame.K_s]:
            self.move(dt, Direction.BACKWARD)
        if keys[pygame.K_a]:
            self.rotate(dt, Direction.LEFT)
        if keys[pygame.K_d]:
            self.rotate(dt, Direction.RIGHT)

        if keys[pygame.K_SPACE]:
            self.shoot()



    def shoot(self):

        if self.timer > 0:
            return

        shoot_vel = pygame.Vector2(0, 1).rotate(self.rotation)
        shoot_vel *= PLAYER_SHOOT_SPEED

        new_bullet = Shot(self.position.x, self.position.y, shoot_vel)

        self.timer = 0.3

        