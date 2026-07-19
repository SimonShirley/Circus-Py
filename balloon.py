import pygame

class Balloon:
    # Initial balloon position
    ballon_width, balloon_height = 10, 10
    balloon_position: pygame.Vector2 = pygame.Vector2(0, 0)
    move_speed: int = 150
    direction: int = 1
    _active: bool = True


    def __init__(self, x: int, y: int, width: int, height: int) -> Balloon:
        width = width if width > 0 else 1
        height = height if height > 0 else 1

        self.balloon_position = pygame.Vector2(x, y)
        self.ballon_width = width
        self.balloon_height = height


    def has_collided(self, player_rect: pygame.rect.Rect) -> bool:
        balloon_rect = pygame.rect.Rect((self.balloon_position.x, self.balloon_position.y), (self.ballon_width, self.balloon_height))

        return balloon_rect.colliderect(player_rect)
    

    def get_active(self) -> bool:
        return self._active

    def set_active(self, state: bool) -> None:
        self._active = state
        

    def update(self, screen: pygame.Surface, delta_time: float):
        self.balloon_position.x += self.move_speed * delta_time

        if self.balloon_position.x > screen.get_width() + self.ballon_width:
            self.balloon_position.x = -self.ballon_width

    
    def draw(self, screen: pygame.Surface) -> None:
        if self._active:
            pygame.draw.rect(screen, "yellow", pygame.rect.Rect(self.balloon_position, (self.ballon_width, self.balloon_height)))