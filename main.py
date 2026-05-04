import pygame
from logger import log_state,log_event
from constants import SCREEN_HEIGHT,SCREEN_WIDTH 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init() 
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print("Screen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (drawable,updatable,shots)
    while True:
        log_state()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        updatable.update(dt)
        for obj in asteroids:
            if obj.colides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if obj.colides_with(shot):
                    log_event("asteroid_shot")
                    obj.split()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()
