import pygame

class Spike():
    def __init__(self, x, y, x_velocity, y_velocity, width=50, height=50, image_path='images/spike.png'):      
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        actual_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(actual_image, (width, height))
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.prev_x, self.prev_y = self.x, self.y
        self.rect = pygame.Rect(x, y, width, height)  


    def move(self, dt):
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def check_out_of_bounds(self, screen_width, screen_height):
        if self.x < 0:
            self.x = 0
            self.x_velocity *= -1
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
            self.x_velocity *= -1
            print('out of bounds')
        if self.y < 0:
            self.y = 0
            self.y_velocity *= -1
        if self.y > screen_height - self.height:
            self.y = screen_height - self.height
            self.y_velocity *= -1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def check_collision_wall(self, wall_list):
        for wall in wall_list:
            if self.rect.colliderect(wall.rect):
                self.x, self.y = self.prev_x, self.prev_y
                self.x_velocity *= -1
                self.y_velocity *= -1
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)