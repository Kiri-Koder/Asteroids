import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        pass
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_vector1 = self.velocity.rotate(random.uniform(20, 50)) * 1.2
            new_vector2 = self.velocity.rotate(random.uniform(-20, -50)) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid1.velocity = new_vector1
            asteroid2.velocity = new_vector2


