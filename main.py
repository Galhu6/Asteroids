import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

pygame.init()
clock = pygame.time.Clock()
dt = 0


Player.containers = (updatable, drawable)
Shot.containers = (shots, updatable, drawable)


player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def main():
    global dt
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    asteroids  = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill((0, 0, 0))
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game Over!")
                running = False
        
            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()

if __name__ == "__main__":
    main()