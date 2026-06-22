import pygame
from circleshape import CircleShape
import constants
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
        pass
    
    def update(self, dt):
        self.position += (self.velocity * dt)
