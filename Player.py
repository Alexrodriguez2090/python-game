import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Loading player animations
        self.idleUpFrames = []
        for i in range(1,5):
            self.idleUpFrames.append(pygame.image.load(f"images/character/idle/idle up{i}.png").convert_alpha())

        self.idleDownFrames = []
        for i in range(1,5):
            self.idleDownFrames.append(pygame.image.load(f"images/character/idle/idle down{i}.png").convert_alpha())

        self.idleLeftFrames = []
        for i in range(1,5):
            self.idleLeftFrames.append(pygame.image.load(f"images/character/idle/idle left{i}.png").convert_alpha())

        self.idleRightFrames = []
        for i in range(1,5):
            self.idleRightFrames.append(pygame.image.load(f"images/character/idle/idle right{i}.png").convert_alpha())
        
        
        self.walkUpFrames = []
        for i in range(1,5):
            self.walkUpFrames.append(pygame.image.load(f"images/character/walk/walk up{i}.png").convert_alpha())

        self.walkDownFrames = []
        for i in range(1,5):
            self.walkDownFrames.append(pygame.image.load(f"images/character/walk/walk down{i}.png").convert_alpha())

        self.walkLeftFrames = []
        for i in range(1,5):
            self.walkLeftFrames.append(pygame.image.load(f"images/character/walk/walk left{i}.png").convert_alpha())

        self.walkRightFrames = []
        for i in range(1,5):
            self.walkRightFrames.append(pygame.image.load(f"images/character/walk/walk right{i}.png").convert_alpha())

        self.frames = 3
        self.animationIndex = 0



        #Starting player variables and image
        self.image = self.idleDownFrames[self.animationIndex]
        self.surface = pygame.transform.scale2x(self.image)
        self.rect = self.surface.get_rect(midbottom = (300, 300))
        self.direction = "d"
        self.action = "i"
    
    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.top -= 1
            self.direction = "u"
            self.action = "m"
        if keys[pygame.K_s]:
            self.rect.top += 1
            self.direction = "d"
            self.action = "m"
        if keys[pygame.K_a]:
            self.rect.left -= 1
            self.direction = "l"
            self.action = "m"
        if keys[pygame.K_d]:
            self.rect.left += 1
            self.direction = "r"
            self.action = "m"
    
    def changeSprite(self):
        if self.animationIndex >= self.frames:
            self.animationIndex = 0
        else:
            self.animationIndex += 0.1

        if self.direction == "u":
            if self.action == "i":
                self.image = self.idleUpFrames[int(self.animationIndex)]
            elif self.action == "m":
                self.image = self.walkUpFrames[int(self.animationIndex)]

        elif self.direction == "d":
            if self.action == "i":
                self.image = self.idleDownFrames[int(self.animationIndex)]
            elif self.action == "m":
                self.image = self.walkDownFrames[int(self.animationIndex)]

        elif self.direction == "l":
            if self.action == "i":
                self.image = self.idleLeftFrames[int(self.animationIndex)]
            elif self.action == "m":
                self.image = self.walkLeftFrames[int(self.animationIndex)]

        else:
            if self.action == "i":
                self.image = self.idleRightFrames[int(self.animationIndex)]
            elif self.action == "m":
                self.image = self.walkRightFrames[int(self.animationIndex)]

    def update(self):
        self.action = "i"
        self.playerInput()
        self.changeSprite()
