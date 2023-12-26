import pygame
from objects.colors import *

# Importing level 2 objects
from levels.level_objects.level_3_objects import *

# Level 2 function
def level_3(death, screen, screen_image, clock, dt, screen_width, screen_height):
    running = True
    quit = False

    # Pausing the game for a second
    screen.fill(BLACK)
    pygame.time.delay(50)

    # Main Game Loop
    while running:
        # Quitting the level if the user presses the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        if quit:
            pygame.quit()

        """
        Player Movement
        """ 
        # Saving the previous position of the player for collision detection
        player.prev_x, player.prev_y = player.x, player.y
        player.move(dt)

        """
        Spike Movement
        """
        # Saving the previous position of the spike for collision detection
        for spike in spike_list:
            spike.prev_x, spike.prev_y = spike.x, spike.y
        for spike in spike_list:
            spike.move(dt)
        """
        Collision Detection
        """
        # Player Collision Detection
        player.check_out_of_bounds(screen_width, screen_height)
        death.count = player.check_collision_spike(spike_list, death.count)
        player.check_collision_wall(wall_list)
        running = player.check_goal(Goal)

        # Spike Collision Detection
        for spike in spike_list:
            spike.check_out_of_bounds(screen_width, screen_height)
            spike.check_collision_wall(wall_list)

        """
        Drawing Game Objects
        """
        # Clear screen
        screen.fill(WHITE)
        
        # Draw background
        screen.blit(screen_image, (0, 0))
        # Draw player
        screen.blit(player.image, (player.x, player.y))
        # Draw spike
        for spike in spike_list:
            screen.blit(spike.image, (spike.x, spike.y))
        # Draw walls
        for wall in wall_list:
            screen.blit(wall.image, (wall.x, wall.y))
        # Draw goal
        screen.blit(Goal.image, (Goal.x, Goal.y))

        # Draw death counter
        death_text = pygame.font.SysFont('Arial', 30).render(f'Deaths: {death.count}', True, WHITE)
        death.counter_surface.fill(BLACK)
        death.counter_surface.blit(death_text, (0, 10))
        screen.blit(death.counter_surface, (0, 0))

        # Update display
        pygame.display.update()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

    return death