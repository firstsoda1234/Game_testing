import pygame
import sys
import os

#GEOMETRY
WIDTH = 500
HIGHT = 750
FPS = 60 # Frame rate per second

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LOW_BROWN = (66, 65, 61)
sea_blue = (161, 246, 247)


#initialize PYGAME
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("BIG TU SUBMARINE")
clock = pygame.time.Clock()

#############CREATE SUBMARINE #############
game_folder = os.path.dirname('C:\Python\yourselfcode\my_code\Wirting-game/')
img_folder = os.path.join(game_folder, 'img')
print(img_folder)

"""heelo = os.getcwd()
im_f = os.path.join(heelo, 'img')
print(im_f)
"""
class Submarine(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50,50))
        sub_img = os.path.join(img_folder,'submarine.png')
        self.image = pygame.image.load(sub_img).convert()
        self.image.set_colorkey(BLACK) #ตัดสี background ของรููปภาพออก
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HIGHT - 12

        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5

        if keystate[pygame.K_RIGHT]:
            self.speedx = 5

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speedx

        #print(self.rect.x)

# sprite is a player
all_sprites = pygame.sprite.Group()
submarine = Submarine()
all_sprites.add(submarine)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        #check for closing
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(sea_blue)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()