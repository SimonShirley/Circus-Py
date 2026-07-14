# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen_size = screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
delta_time = 0

# Initial player position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def update():
    global player_pos, delta_time

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos.y -= 300 * delta_time
    if keys[pygame.K_s]:
        player_pos.y += 300 * delta_time
    if keys[pygame.K_a]:
        player_pos.x -= 300 * delta_time
    if keys[pygame.K_d]:
        player_pos.x += 300 * delta_time


def draw():
    global screen
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkblue")

    pygame.draw.circle(screen, "red", player_pos, 40)

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