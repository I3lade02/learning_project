import pygame
import random

class FallingObject:
    def __init__(self, screen_width, screen_height, color, life_reduction = False):
        self.width = 30
        self.height = 30
        self.x = random.randint(0, screen_width - self.width)
        self.y = -self.height
        self.speed = random.randint(3, 6)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = color
        self.life_reduction = life_reduction

    def update(self):
        self.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def reset_position(self):
        self.y = -self.height
        self.x = random.randint(0, self.screen_width - self.width)

class GreenBrick(FallingObject):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, (0, 255, 0), life_reduction = True)