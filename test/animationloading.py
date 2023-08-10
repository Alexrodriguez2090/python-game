#Finding ways to import animations more cleanly

import os
import pygame

pygame.init()
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

directory = "images/character/idle/down/"
myList = [pygame.image.load(directory + image).convert_alpha() for image in os.listdir(directory)]

"""self.animations = {"idleUp": [], "idleDown": [], "idleLeft": [], "idleRight": [], "walkUp": [], "walkDown": [], "walkLeft": [],
                      "walkRight": []}

for i in range(1,5):
    self.animations["idleUp"].append(pygame.image.load(f"images/character/idle/idle up{i}.png").convert_alpha())"""

print(myList)