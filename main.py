import pygame
from player import Player
from falling_object import FallingObject, GreenBrick  # Correct import for GreenBrick
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Frame rate
clock = pygame.time.Clock()
fps = 60

# Function to display the menu
def show_menu():
    font = pygame.font.SysFont(None, 50)
    title_text = font.render("Catch the Falling Objects", True, blue)
    start_text = font.render("Press 'Enter' to Start", True, black)
    settings_text = font.render("Press 'Space' for Settings", True, black)
    quit_text = font.render("Press 'Q' to Quit", True, black)
    
    screen.fill(white)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 4))
    screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2 - 50))
    screen.blit(settings_text, (screen_width // 2 - settings_text.get_width() // 2, screen_height // 2))
    screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, screen_height // 2 + 50))
    pygame.display.update()

# Function to display the settings screen
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

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # If player presses 'Esc', return to the main menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    show_menu()

# Main game loop
def game_loop():
    player = Player(screen_width, screen_height)
    falling_objects = [FallingObject(screen_width, screen_height, (255, 0, 0)) for _ in range(5)]  # Red falling objects
    green_bricks = [GreenBrick(screen_width, screen_height) for _ in range(2)]  # Green bricks that reduce life
    score = 0
    lives = 3  # Player starts with 3 lives
    game_paused = False  # Variable to track if the game is paused

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause when 'P' is pressed
                    game_paused = not game_paused
                if event.key == pygame.K_q:  # Quit when 'Q' is pressed
                    pygame.quit()
                    quit()

        screen.fill(white)

        # Pause screen
        if game_paused:
            pause_screen()
            continue

        # Handle player movement
        player.handle_movement()

        # Update and draw falling objects (red)
        for obj in falling_objects:
            obj.update()
            obj.draw(screen)

            if player.check_collision(obj):
                score += 1
                obj.reset_position()

            # If object falls below the screen, reset it
            if obj.y > screen_height:
                obj.reset_position()

        # Update and draw green bricks (which reduce life)
        for green_brick in green_bricks:
            green_brick.update()
            green_brick.draw(screen)

            if player.check_collision(green_brick):
                lives -= 1  # Reduce life when a green brick is caught
                green_brick.reset_position()

            # If green brick falls below the screen, reset it
            if green_brick.y > screen_height:
                green_brick.reset_position()

        # Draw player
        player.draw(screen)

        # Display score and lives
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, black)
        lives_text = font.render(f"Lives: {lives}", True, black)
        screen.blit(score_text, [10, 10])
        screen.blit(lives_text, [screen_width - 100, 10])

        # If player runs out of lives, show game over screen
        if lives <= 0:
            game_over_screen(score)
            break

        # Update the screen
        pygame.display.update()

        # Control the frame rate
        clock.tick(fps)

# Function to display pause screen
def pause_screen():
    font = pygame.font.SysFont(None, 60)
    paused_text = font.render("Paused", True, (0, 0, 0))
    quit_text = font.render("Press 'Q' to Quit", True, (0, 0, 0))
    screen.blit(paused_text, (screen_width // 2 - paused_text.get_width() // 2, screen_height // 2 - paused_text.get_height() // 2))
    screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, screen_height // 2 + 50))
    pygame.display.update()

# Function to display game over screen
def game_over_screen(score):
    font = pygame.font.SysFont(None, 50)
    game_over_text = font.render(f"Game Over! Score: {score}", True, (0, 0, 0))
    restart_text = font.render("Press 'R' to Restart", True, (0, 0, 0))
    quit_text = font.render("Press 'Q' to Quit", True, (0, 0, 0))

    screen.fill(white)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 50))
    screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, screen_height // 2 + 100))
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

# Start the game
def main():
    # Display the menu first
    show_menu()

    # Wait for player to start the game, show settings or quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # If player presses Enter, start the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False  # Break the loop to start the game
                    game_loop()

                # If player presses Space, show the settings screen
                if event.key == pygame.K_SPACE:
                    show_settings()

                # If player presses 'Q', quit the game
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                # If player presses 'Esc', return to the main menu
                if event.key == pygame.K_ESCAPE:
                    show_menu()

# Run the game
if __name__ == "__main__":
    main()
