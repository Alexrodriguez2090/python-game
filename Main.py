import os
import pygame
import Player


pygame.init()

screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
groundSurface = pygame.transform.scale(pygame.image.load("images/bg.png").convert(), (screenWidth,screenHeight))

player = pygame.sprite.GroupSingle()
player.add(Player.Player())

#obstacles = pygame.sprite.Group()

startButtonText = pygame.font.Font(None, 50)
startButtonTextSurface = startButtonText.render("Start", False, (60, 60, 60))
startButtonRect = startButtonTextSurface.get_rect(center = (screenWidth/2, screenHeight/2))

clock = pygame.time.Clock()
running = True
deltaTime = 0
gameState = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if gameState == 0: #Game is active
        #Screen fills
        screen.fill("grey")
        screen.blit(groundSurface, (0,0))


        #Player
        player.draw(screen)
        player.update()

        if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
            gameState = 1

    elif gameState == 1: #Menu
        #Screen fills
        screen.fill("grey")

        #pygame.draw.rect(screen, "Red", startButtonRect)
        pygame.draw.rect(screen, "Red", startButtonRect, border_radius=10)
        screen.blit(startButtonTextSurface, startButtonRect)
        

        #Controls
        mousePos = pygame.mouse.get_pos()
        if startButtonRect.collidepoint(mousePos) and pygame.mouse.get_pressed()[0] == True:
            gameState = 0
    
    elif gameState == 2: #Pause menu
        pass


    #Running the game
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000

pygame.quit()