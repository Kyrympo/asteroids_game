import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH 
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init() 
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print("Screen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2 
    player = Player(player_x,player_y,0)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    asteroidFieldSprite = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,drawable,updatable)
    while True:
        screen.fill('black')
        
        updatable.update(dt)
        for obj in asteroids:
            if obj.collides_with(player):
                log_event('player_hit')
                print('Game over!')
                sys.exit()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        #print(dt)
if __name__ == "__main__":
    main()
