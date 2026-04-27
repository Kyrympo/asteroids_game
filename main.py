import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH 
from logger import log_state


def main():
    pygame.init() 
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print("Screen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        screen.fill('black')
        pygame.display.flip()
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        #print(dt)
if __name__ == "__main__":
    main()
