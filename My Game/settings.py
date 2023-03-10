# This file contains the main settings 
# of the game that the player is able to change
import pygame

# Display Size
screen_width = 1200
screen_height = 700

# Size of the main chararcter sprite
block_width = 50
block_height = 50

# Movement Speed
player_speed = 5

# Clock tick rate
tick_rate = 60

# Temp Game map
game_map = [["","X","","","","","","","","","","","","","","","","","","","","","",""],
["","X","","","","","","","","","","","","","","","","","","","","","",""],
["","X","P","","","","","","","","","","","","","","","","","","","","",""],
["","X","","","","","","","","","","","","","","","","","","","","","",""],
["","X","","","","","","","","","","","","","","","","","","","","","",""],
["","X","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","",""],
["","","X","X","X","","","X","X","X","X","X","X","X","X","X","X","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","X","","","","X","","","","","","","","","","","","",""],
["","","","","","","X","X","X","X","","","X","","","","","","","","","","",""],
["","","","","","","","","","","","","","X","","","","","","X","","","",""],
["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
]

# Gravity

gravity = 5