# Example file showing a basic pygame "game loop"
import pygame, player, balloon, logging

# pygame setup
pygame.init()
screen_size = screen_width, screen_height = 1280, 720
screen: pygame.Surface = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Circus Py, by Alto Fluff")
clock: pygame.Clock = pygame.time.Clock()
running: bool = True
delta_time: float = 0
player = player.Player(screen_width / 25, screen_width / 25)
balloon_list: list[balloon.Balloon] = []
balloon_line_count: int = 25
balloon_width: float = screen_width / (balloon_line_count * 2)

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(level=logging.DEBUG)
formatter =  logging.Formatter('%(levelname)s : %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

for i in range(0, 3):
    for j in range(0, balloon_line_count + 1):
        balloon_list.append(balloon.Balloon((j * balloon_width * 2), (i * balloon_width * 2) + balloon_width, balloon_width, balloon_width))



logger.debug('simple message')

def update() -> None:
    global screen, delta_time

    player.update(screen, delta_time)

    for balloon in balloon_list:
        balloon.update(screen, 0.02)

        if balloon.get_active():
            balloon_collision: bool = balloon.has_collided(player.get_bounding_rect())

            if balloon_collision:
                balloon.set_active(False)


def draw() -> None:
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