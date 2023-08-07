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
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.direction = "d"
        self.action = "i"
        self.speed = 2
    
    def playerInput(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt
            self.rect.y = round(self.pos.y)
            self.direction = "u"
            self.action = "m"
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt
            self.rect.y = round(self.pos.y)
            self.direction = "d"
            self.action = "m"
        if keys[pygame.K_a]:
            self.pos.x -= self.speed * dt
            self.rect.x = round(self.pos.x)
            self.direction = "l"
            self.action = "m"
        if keys[pygame.K_d]:
            self.pos.x += self.speed * dt
            self.rect.x = round(self.pos.x)
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

    def update(self, dt):
        self.action = "i"
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.playerInput(dt)
        self.changeSprite()
