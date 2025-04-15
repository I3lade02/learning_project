import pygame
class Player:
    def __init__(self, screen_width, screen_height):
        self.width = 50
        self.height = 50
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height - self.height - 10
        self.speed = 7
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), [self.x, self.y, self.width, self.height])

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < self.screen_width - self.width:
            self.x += self.speed

    def check_collision(self, falling_object):
        if (falling_object.x < self.x + self.width and 
            falling_object.x + falling_object.width > self.x and
            falling_object.y + falling_object.height > self.y):
            return True
        return False