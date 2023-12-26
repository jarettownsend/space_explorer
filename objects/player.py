import pygame

class Player():
    def __init__(self, x, y, width=50, height=50):
        self.starting_position = (x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        actual_image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(actual_image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.prev_x, self.prev_y = self.x, self.y


    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 200 * dt
        if keys[pygame.K_DOWN]:
            self.y += 200 * dt
        if keys[pygame.K_RIGHT]:
            self.x += 200 * dt
        if keys[pygame.K_LEFT]:
            self.x -= 200 * dt
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
   
    def check_collision_wall(self, wall_list):
        leeway = 10
        player_rect_with_leeway = self.rect.inflate(-leeway, -leeway)
        for wall in wall_list:
            if player_rect_with_leeway.colliderect(wall.rect):
                self.x, self.y = self.prev_x, self.prev_y
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision_spike(self, spike_list, death_count):
        leeway = 30
        player_rect_with_leeway = self.rect.inflate(-leeway, -leeway)
        for spike in spike_list:
            if player_rect_with_leeway.colliderect(spike.rect):
                death_count += 1
                pygame.time.delay(25)
                self.x, self.y = self.starting_position
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return death_count
            
    
    def check_out_of_bounds(self, screen_width, screen_height):
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
        if self.y < 0:
            self.y = 0
        if self.y > screen_height - self.height:
            self.y = screen_height - self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def check_goal(self, goal):
        leeway = 10
        player_rect_with_leeway = self.rect.inflate(-leeway, -leeway)
        if player_rect_with_leeway.colliderect(goal.rect):
            return False
        return True
