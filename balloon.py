import pygame

class Balloon:
    # Initial balloon position
    ballon_width, balloon_height = 10, 10
    balloon_position: pygame.Vector2 = pygame.Vector2(0, 0)
    move_speed: int = 150
    direction: int = 1


    def __init__(self, x: int, y: int, width: int, height: int):
        width = width if width > 0 else 1
        height = height if height > 0 else 1

        self.balloon_position = pygame.Vector2(x, y)
        self.ballon_width = width
        self.balloon_height = height
        

    def update(self, screen: pygame.Surface, delta_time: float):
        self.balloon_position.x += self.move_speed * delta_time

        if self.balloon_position.x > screen.get_width() + self.ballon_width:
            self.balloon_position.x = -self.ballon_width

    
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "yellow", pygame.rect.Rect(self.balloon_position, (self.ballon_width, self.balloon_height)))