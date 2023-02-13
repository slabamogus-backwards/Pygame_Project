import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.image = pygame.Surface((size[0], size[1]))
        self.rect = self.image.get_rect(topleft = pos)
        self.image = pygame.image.load("Final Project/Assests/Player.png").convert()
        self.x_direction = 0
        self.y_direction = 0
    
    def get_input(self):
        # For x-direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_direction = player_speed
        elif keys[pygame.K_LEFT]:
            self.x_direction = -player_speed
        else:
            self.x_direction = 0  

        # For y-direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.y_direction = player_speed
        elif keys[pygame.K_UP]:
            self.y_direction = -player_speed
        else:
            self.y_direction = 0

    def boundary_check(self):
        # Border Check
        if self.rect.x > screen_width - block_width:
            self.rect.x = screen_width - block_width
        elif self.rect.x < 0:
            self.rect.x = 0
        
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > screen_height - block_height:
            self.rect.y = screen_height - block_height

    def update(self):
        self.get_input()
        self.rect.y += self.y_direction
        self.rect.x += self.x_direction
        self.boundary_check()
