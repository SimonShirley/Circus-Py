# Example file showing a basic pygame "game loop"
import pygame, acrobat, balloon, logging, console_logger
import math

# pygame setup
pygame.init()
screen_size = screen_width, screen_height = 1280, 720
screen: pygame.Surface = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Circus Py, by Alto Fluff")
clock: pygame.Clock = pygame.time.Clock()
running: bool = True
delta_time: float = 0
player = acrobat.Acrobat(screen_width / 25, screen_width / 25, pygame.Vector2(0, 500))
balloon_list: list[balloon.Balloon] = []
balloon_active_list: list[int] = []
balloon_row_count: int = 3
balloon_line_count: int = 26
balloon_width: float = screen_width / ((balloon_line_count - 1) * 2)

for i in range(0, balloon_row_count):
    balloon_active_list.append(balloon_line_count)

    for j in range(0, balloon_line_count):
        balloon_list.append(balloon.Balloon((j * balloon_width * 2), (i * balloon_width * 2) + balloon_width, balloon_width, balloon_width))

logger: logging.Logger = console_logger.Logger().get_logger()
logger.debug('simple message')

def decrease_balloon_row_count(balloon_index: int):
    global balloon_line_count, balloon_active_list

    balloon_row_index = math.floor(balloon_index / balloon_line_count)
    balloon_active_list[balloon_row_index] -= 1

def reactivate_balloon_row(row_index: int):
    global balloon_list, balloon_active_list

    balloon_row_offset: int = balloon_line_count * row_index
 
    for balloon_index in range(balloon_row_offset, balloon_row_offset + balloon_line_count):
        balloon_list[balloon_index].set_active(True)

    balloon_active_list[row_index] = balloon_line_count


def update() -> None:
    global screen, delta_time

    player.update(screen, delta_time)

    for balloon in balloon_list:
        balloon.update(screen, 0.02)

        if balloon.get_active():
            balloon_collision: bool = balloon.has_collided(player.get_bounding_rect())

            if balloon_collision:
                balloon.set_active(False)
                decrease_balloon_row_count(balloon_list.index(balloon))
                
                for balloon_row in range(0, balloon_row_count):
                    if balloon_active_list[balloon_row] == 0:
                        reactivate_balloon_row(balloon_row)
                        


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