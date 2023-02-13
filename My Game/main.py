# Init game settings / controls
import pygame, sys
from player import Player
from barriers import Barriers
from settings import *

# Init game surface and clock
screen = pygame.display.set_mode((screen_width, screen_height))

# Player sprite
player_sprites = pygame.sprite.Group()

# Barrier sprite
barrier_sprites = pygame.sprite.Group()

for row_index , row in enumerate(game_map):
    for col_index , col in enumerate(row):
        if col == "X":
            wall = Barriers((block_width , block_height) , (col_index * block_width , row_index * block_height))
            barrier_sprites.add(wall)
        elif col == "P":
            #instantiating player sprite
            player = Player((block_width , block_height) , (col_index * block_width , row_index * block_height))
            player_sprites.add(player)

clock = pygame.time.Clock()

# Flag for game loop
run = True

# Main game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((52, 97, 97))
    player_sprites.draw(screen)
    barrier_sprites.draw(screen)
    
    pygame.display.update()
    player_sprites.update(barrier_sprites)
    clock.tick(tick_rate)