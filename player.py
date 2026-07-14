import pygame

class Player:
    # Initial player position
    player_size = player_width, player_height = 100, 100
    player_pos: pygame.Vector2 = pygame.Vector2(0, 0)
    screen: pygame.Surface = pygame.Surface((0, 0))


    def __init__(self, width: int, height: int, screen: pygame.Surface):
        self.player_pos = pygame.Vector2(width / 2, height / 2)
        self.screen = screen
        

    def update(self, delta_time: float):
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

        if self.player_pos.x > self.screen.get_width() - half_width:
            self.player_pos.x = self.screen.get_width() - half_width
        if self.player_pos.x < half_width:
            self.player_pos.x = half_width
        if self.player_pos.y > self.screen.get_height() - half_height:
            self.player_pos.y = self.screen.get_height() - half_height
        if self.player_pos.y < half_height:
            self.player_pos.y = half_height

    
    def draw(self):
        pygame.draw.circle(self.screen, "red", self.player_pos, self.player_width / 2)