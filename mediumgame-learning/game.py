import pygame
from pygame.math import Vector2
from pygame import Rect

class GameState:
    def __init__(self):
        self.worldSize = Vector2(16, 10)
        self.tankPos = Vector2(0, 0)
        self.tower1Pos = Vector2(10, 3)
        self.tower2Pos = Vector2(10, 5)

    def update(self, moveTankCommand):
        newTankPos = self.tankPos + moveTankCommand

        if 0 <= newTankPos.x < self.worldSize.x \
        and 0 <= newTankPos.y < self.worldSize.y \
        and newTankPos != self.tower1Pos and newTankPos != self.tower2Pos:
            self.tankPos = newTankPos

class UserInterface:
    def __init__(self):
        pygame.init()

        # Game state
        self.gameState = GameState()

        # Rendering properties
        self.cellSize = Vector2(64, 64)
        self.unitsTexture = pygame.image.load('units.png')

        #Window
        windowSize = self.gameState.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x), int(windowSize.y)))
        pygame.display.set_caption('GameTank')
        pygame.display.set_icon(pygame.image.load('icon.png'))

        self.moveTankCommand = Vector2(0, 0)


        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

    def processInput(self):
        self.moveTankCommand = Vector2(0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.moveTankCommand.x = 1
                elif event.key == pygame. K_LEFT:
                    self.moveTankCommand.x = -1
                elif event.key == pygame. K_DOWN:
                    self.moveTankCommand.y = 1
                elif event.key == pygame.K_UP:
                    self.moveTankCommand.y = -1

    def update(self):
        self.gameState.update(self.moveTankCommand)

    def render(self):
        self.window.fill('black')

        # Tank base
        spritePoint = self.gameState.tankPos.elementwise()*self.cellSize
        texturePoint = Vector2(1, 0).elementwise()* self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitsTexture, spritePoint, textureRect)

        # Tower 1
        spritePoint = self.gameState.tower2Pos.elementwise()*self.cellSize
        texturePoint = Vector2(0, 1).elementwise()*self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitsTexture, spritePoint, textureRect)
        texturePoint = Vector2(0, 6).elementwise()*self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitsTexture, spritePoint, textureRect)
        
        # Tower 2
        spritePoint = self.gameState.tower1Pos.elementwise() * self.cellSize
        texturePoint = Vector2(0, 1).elementwise() * self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitsTexture, spritePoint, textureRect)
        texturePoint = Vector2(0, 6).elementwise() * self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitsTexture, spritePoint, textureRect)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

userInterface = UserInterface()
userInterface.run()

pygame.quit()