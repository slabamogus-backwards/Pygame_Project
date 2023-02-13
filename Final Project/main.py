import pygame, sys
import math
from Player import *
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))

scroll = 0

clock = pygame.time.Clock()
bg = pygame.image.load("Final Project/Assests/River/PNG/background.png")
bg_height = bg.get_height()
tiles = math.ceil(screen_height/bg_height) + 1

player_sprites = pygame.sprite.Group()
player = Player((block_width, block_height), (screen_width / 2, screen_height / 2))
player_sprites.add(player)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for x in range(tiles):
        screen.blit(bg, (0,((x * bg_height) - screen_height + scroll)))

    scroll += 1

    if abs(scroll) > bg_height:
        scroll = 0
    
    player_sprites.draw(screen)
    pygame.display.update()
    player_sprites.update()
    clock.tick(60)

