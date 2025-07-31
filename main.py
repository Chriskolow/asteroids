import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_KINDS
from constants import ASTEROID_SPAWN_RATE
from constants import ASTEROID_MAX_RADIUS
from constants import PLAYER_RADIUS
from player import Player
from constants import PLAYER_TURN_SPEED
from asteroid import Asteroid
from asteroidfield import AsteroidField
from cricleshape import CircleShape 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black = (0,0,0)
        screen.fill(black)
        dt = clock.tick(60) /1000
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    main()
