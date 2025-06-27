import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
         super().__init__(position.x, position.y, radius, velocity)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity_one = self.velocity.rotate(random_angle) * 1.2
        new_velocity_two = self.velocity.rotate(-random_angle) * 1.2
        new_asteroid_one = Asteroid(self.position, new_radius, new_velocity_one)
        new_asteroid_two = Asteroid(self.position, new_radius, new_velocity_two)
        return new_asteroid_one, new_asteroid_two
