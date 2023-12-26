import pygame
from objects.colors import *

def credits(screen, screen_image, screen_width, death):
    running = True
    quit = False

    # Main Game Loop
    while running:
        # Quitting the level if the user presses the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        if quit:
            pygame.quit()
        
        # Quit the game if Space is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = False

        # Having the background image
        screen.blit(screen_image, (0, 0))

        # Displaying the title
        title_font = pygame.font.SysFont('Arial', 100)
        title = title_font.render('Congratulations! You Win!', True, GREEN)
        screen.blit(title, (screen_width / 2 - title.get_width() / 2, 100))

        # Displaying the instructions
        instructions_font = pygame.font.SysFont('Arial', 30)
        instructions = instructions_font.render(f'You beat Space Explorer with {death.count} deaths', True, GREEN)
        screen.blit(instructions, (screen_width / 2 - instructions.get_width() / 2, 300))

        # Update display
        pygame.display.update()