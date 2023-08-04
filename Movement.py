import pygame

def player(playerRect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerRect.top -= 1
    if keys[pygame.K_s]:
        playerRect.top += 1
    if keys[pygame.K_a]:
        playerRect.left -= 1
    if keys[pygame.K_d]:
        playerRect.left += 1