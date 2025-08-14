import sys
import pygame
from constants import *
from circleshape import CircleShape
from player import *
from asteroidfield import *
from asteroid import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroidfield = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for art in drawable:
            art.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
