import pygame
from player import Player
from falling_object import FallingObject
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cath the falling objects")

white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()
fps = 60

def game_loop():
    player = Player(screen_width, screen_height)
    falling_objects = [FallingObject(screen_width, screen_height) for _ in range(5)]
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        screen.fill(white)

        player.handle_movement()

        for obj in falling_objects:
            obj.update()
            obj.draw(screen)


            if player.check_collision(obj):
                score += 1
                obj.reset_position()

            if obj.y > screen_height:
                obj.reset_position()
        
        player.draw(screen)

        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, [10, 10])

        pygame.display.update()

        clock.tick(fps)

game_loop()