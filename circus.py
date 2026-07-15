# Example file showing a basic pygame "game loop"
import pygame, player, balloon, logging

# pygame setup
pygame.init()
screen_size = screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
delta_time = 0
player = player.Player(100, 100)
balloon_list = []
balloon_line_count = 21
balloon_width = screen_width / ((balloon_line_count - 1) * 2)

for i in range(0, balloon_line_count):
    balloon_list.append(balloon.Balloon((i * balloon_width * 2), balloon_width, balloon_width, balloon_width))

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(level=logging.DEBUG)
formatter =  logging.Formatter('%(levelname)s : %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

logger.debug('simple message')

def update():
    global screen, delta_time

    for balloon in balloon_list:
        balloon.update(screen, delta_time)

    player.update(screen, delta_time)


def draw():
    global screen
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkblue")

    for balloon in balloon_list:
        balloon.draw(screen)

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