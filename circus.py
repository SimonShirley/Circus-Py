# Example file showing a basic pygame "game loop"
import pygame, player

# pygame setup
pygame.init()
screen_size = screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
delta_time = 0
player = player.Player(100, 100)

def update():
    global screen, delta_time

    player.update(screen, delta_time)


def draw():
    global screen
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkblue")

    player.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    update()
    draw()

    # limits FPS to 60
    # delta time in seconds since last frame, used for framerate-
    # independent physics.
    delta_time = clock.tick(60) / 1000


pygame.quit()