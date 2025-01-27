import pygame
from circleshape import CircleShape
from constants import SHOOT_RADIUS


class Shoot(CircleShape):
    def __init__(self, x, y, radius=SHOOT_RADIUS):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
