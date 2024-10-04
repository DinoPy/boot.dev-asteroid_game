import pygame
from random import uniform
from circleshape import CircleShape
from shoot import Shoot
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        angle = uniform(20, 50)
        asteroid1 = Asteroid(
            *self.position, (self.radius - ASTEROID_MIN_RADIUS))
        asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid2 = Asteroid(*self.position, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
