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
blue = (0, 0, 255)

clock = pygame.time.Clock()
fps = 60

def show_menu():
    font = pygame.font.SysFont(None, 50)
    title_text = font.render("Catch the Falling Objects", True, blue)
    start_text = font.render("Press 'Enter' to Start", True, black)
    settings_text = font.render("Press 'Space' for settings", True, black)
    quit_text = font.render("Press 'Q' to Quit", True, black)
    
    screen.fill(white)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 4))
    screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2))
    screen.blit(settings_text, (screen_width // 2 - settings_text.get_width() // 2, screen_height // 2 + 50))
    screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, screen_height // 2 + 100))
    pygame.display.update()

def show_settings():
    font = pygame.font.SysFont(None, 40)
    controls_title = font.render("Game Controls", True, blue)
    controls_text_1 = font.render("Press 'Enter' to Start the Game", True, black)
    controls_text_2 = font.render("Press 'P' to Pause the Game", True, black)
    controls_text_3 = font.render("Press 'Q' to Quit the Game", True, black)
    controls_text_4 = font.render("Press 'Esc' to Return to Menu", True, black)
    
    screen.fill(white)
    screen.blit(controls_title, (screen_width // 2 - controls_title.get_width() // 2, screen_height // 4))
    screen.blit(controls_text_1, (screen_width // 2 - controls_text_1.get_width() // 2, screen_height // 2 - 100))
    screen.blit(controls_text_2, (screen_width // 2 - controls_text_2.get_width() // 2, screen_height // 2 - 50))
    screen.blit(controls_text_3, (screen_width // 2 - controls_text_3.get_width() // 2, screen_height // 2))
    screen.blit(controls_text_4, (screen_width // 2 - controls_text_4.get_width() // 2, screen_height // 2 + 50))
    pygame.display.update()

def game_loop():
    player = Player(screen_width, screen_height)
    falling_objects = [FallingObject(screen_width, screen_height) for _ in range(5)]
    score = 0
    game_paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_paused = not game_paused
        
        screen.fill(white)

        if game_paused:
            pause_screen()
            continue

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

def pause_screen():
    font = pygame.font.SysFont(None, 60)
    paused_text = font.render("Paused", True, (0, 0, 0))
    screen.blit(paused_text, (screen_width // 2 - paused_text.get_width() // 2, screen_height // 2 - paused_text.get_height() // 2))
    pygame.display.update()

def main():
    show_menu()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    game_loop()

                if event.key == pygame.K_SPACE:
                    show_settings()

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

if __name__ == "__main__":
    main()