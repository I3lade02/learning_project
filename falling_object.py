import pygame
import random

class FallingObject:
    def __init__(self, screen_width, screen_height):
        self.width = 30
        self.height = 30
        self.x = random.randint(0, screen_width - self.width)
        self.y = -self.height
        self.speed = random.randint(3, 6)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        self.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.width, self.height])

    def reset_position(self):
        self.y = -self.height
        self.x = random.randint(0, self.screen_width - self.width)