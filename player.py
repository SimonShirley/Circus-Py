import pygame

class Player:
    # Initial player position
    player_width, player_height = 100, 100
    player_pos: pygame.Vector2 = pygame.Vector2(0, 0)


    def __init__(self, width: int, height: int):
        self.player_pos = pygame.Vector2(width / 2, height / 2)
        self.player_width = width if width > 0 else 1
        self.player_height = height if height > 0 else 1
        

    def update(self, screen: pygame.Surface, delta_time: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * delta_time
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * delta_time
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * delta_time
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * delta_time

        half_width = self.player_width / 2 if self.player_width > 0 else 0
        half_height = self.player_height / 2 if self.player_height > 0 else 0

        if self.player_pos.x > screen.get_width() - half_width:
            self.player_pos.x = screen.get_width() - half_width
        if self.player_pos.x < half_width:
            self.player_pos.x = half_width
        if self.player_pos.y > screen.get_height() - half_height:
            self.player_pos.y = screen.get_height() - half_height
        if self.player_pos.y < half_height:
            self.player_pos.y = half_height

    
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "red", self.player_pos, self.player_width / 2)