import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape):
    #initializing player and hitbox of player
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    #supporting method for the player draw method. player should show as a triangle, even though they will be a CircleShape based object.
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #draws the player using the supporting triangle method when called.
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        pass

    #supporting method for the update method to allow for a rotation of the player ship.
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    #updates positions for player ship based on player input
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    #supporting method for the update method to allow for moving the player ship.
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        player_shot = Shot(self.position[0], self.position[1])
        player_shot.velocity =  pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
