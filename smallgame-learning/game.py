import sys, pygame
from pygame.locals import *



class GameObject:
    def __init__(self, image, height, speed, size_screen: tuple=(500, 400), size_image: tuple=(50, 50)):
        self.image = image
        self.speed = speed
        self.pos = image.get_rect().move(0, height)
        self.size_screen = size_screen
        self.size_image = size_image

    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed

        if self.pos.left < -self.size_image[0]:
            self.pos.left = self.size_screen[0]
        if self.pos.left > self.size_screen[0]:
            self.pos.left = -self.size_image[0]

        if self.pos.top < -self.size_image[1]:
            self.pos.top = self.size_screen[1]
        if self.pos.top > self.size_screen[1]:
            self.pos.top = -self.size_image[1]

pygame.init()

size = width, height = 500, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

background = pygame.image.load('background-(500,400).jpg').convert()
screen.blit(background, (0, 0))

p = pygame.image.load('p.png').convert_alpha()
p = pygame.transform.scale(p, (50, 50))
p = GameObject(p, 50, 3, (500, 400), (50, 50))

# ball = pygame.image.load('intro_ball.png').convert_alpha() # Sem convert() → traduzir a imagem toda vez | Com convert() → traduzir uma vez só e usar direto
# ball = pygame.transform.scale(ball, (50, 50))
# ballrect = ball.get_rect()
# #ballrect = ball.get_rect(center=ballrect.center)

# balls = []
# for n in range(10):
#     o  = GameObject(ball, n*50, n)
#     balls.append(o)


while True:
    screen.blit(background, p.pos, p.pos)
    # for b in balls:
    #     screen.blit(background, b.pos, b.pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys [pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(p.image, p.pos)
    pygame.draw.rect(screen, 'white', p.pos, 2)

    # for b in balls:
    #     b.move()
    #     screen.blit(b.image, b.pos)
    #     pygame.draw.rect(screen, 'white', b.pos, 2)
    pygame.display.flip()
    clock.tick(60)


# isso diz a posicao de cada lado do retângulo
# rect.left / bottom / right / top
# começa em x = 100
#
# começa em y = 50
#
# largura 40
#
# altura 40

#     top = 50
# ┌────────────┐
# │            │
# │            │
# └────────────┘
# left = 100   right = 140
#       bottom = 90
#







