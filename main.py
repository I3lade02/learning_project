import pygame
from player import Player
from falling_object import FallingObject
import random
import json

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the falling objects")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()
fps = 60

def show_menu():
    font = pygame.font.SysFont(None, 50)
    title_text = font.render("Catch the falling object", True, blue)
    start_text = font.render("Press 'Enter' to start", True, black)
    quit_text = font.render("Press 'Q' to Quit", True, black)

    screen.fill(white)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 4))
    screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2))
    screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, screen_height // 2 + 50))
    pygame.display.update()

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

def game_over_screen(score):
    # Load the high score and update if necessary
    high_score = load_high_score()
    if score > high_score:
        high_score = save_high_score(score)
    
    font = pygame.font.SysFont(None, 50)
    game_over_text = font.render(f"Game Over! Score: {score}", True, (0, 0, 0))
    high_score_text = font.render(f"High Score: {high_score}", True, (0, 0, 0))
    restart_text = font.render("Press 'R' to Restart", True, (0, 0, 0))
    quit_text = font.render("Press 'Q' to Quit", True, (0, 0, 0))

    screen.fill(white)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    screen.blit(high_score_text, (screen_width // 2 - high_score_text.get_width() // 2, screen_height // 2 + 50))
    screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 100))
    screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, screen_height // 2 + 150))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    waiting = False
                    game_loop()
                if event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    quit()

# Function to load the high score from a file
def load_high_score():
    try:
        with open('high_score.json', 'r') as file:
            high_score = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        high_score = 0
    return high_score

# Function to save the high score
def save_high_score(score):
    high_score = load_high_score()
    if score > high_score:
        with open('high_score.json', 'w') as file:
            json.dump(score, file)
        return score
    return high_score

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
                
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

if __name__ == "__main__":
    main()