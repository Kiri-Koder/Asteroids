import pygame
import constants
import sys
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print("Hello from asteroids!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    
    #initiating game, declaring variables and groups necessary to display game, player, and asteroids.
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #declaring groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #declaring containers for classes into their groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    field = AsteroidField()
    dt = 0.0
    ship = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    
    #gameplay loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            for shot in shots:
                if shot.collides_with(item) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    item.split()
            if item.collides_with(ship) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 


if __name__ == "__main__":
    main()
