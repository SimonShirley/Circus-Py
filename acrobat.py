import pygame

class Acrobat:
    # Initial player position
    acrobat_width, acrobat_height = 100, 100
    acrobat_pos: pygame.Vector2 = pygame.Vector2(0, 0)
    x_direction: int = 0
    y_direction: int = 1
    speed_amount: int = 300


    def __init__(self, width: int, height: int, start_position: pygame.Vector2) -> None:
        self.acrobat_width = width if width > 0 else 1
        self.acrobat_height = height if height > 0 else 1
        self.acrobat_pos = start_position
        

    def update(self, screen: pygame.Surface, delta_time: float) -> None:
        self.acrobat_pos.x += (self.speed_amount * self.x_direction) * delta_time
        self.acrobat_pos.y += (self.speed_amount * self.y_direction) * delta_time

        half_width = self.acrobat_width / 2 if self.acrobat_width > 0 else 0
        half_height = self.acrobat_height / 2 if self.acrobat_height > 0 else 0

        if self.acrobat_pos.x > screen.get_width() - half_width:
            self.acrobat_pos.x = screen.get_width() - half_width
            self.x_direction *= -1

        if self.acrobat_pos.x < half_width:
            self.acrobat_pos.x = half_width
            self.x_direction *= -1

        if self.acrobat_pos.y > screen.get_height() - half_height:
            self.acrobat_pos.y = screen.get_height() - half_height
            self.y_direction *= -1

            if self.x_direction == 0:
                self.x_direction = 1

        if self.acrobat_pos.y < half_height:
            self.acrobat_pos.y = half_height
            self.y_direction *= -1

    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "red", self.acrobat_pos, self.acrobat_width / 2)

    
    def get_bounding_rect(self) -> pygame.rect.Rect:
        top_left_x: float = self.acrobat_pos.x - (self.acrobat_width / 2)
        top_left_y: float = self.acrobat_pos.y - (self.acrobat_height / 2)

        return pygame.rect.Rect((top_left_x, top_left_y), (self.acrobat_width, self.acrobat_height))