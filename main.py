import pygame
from pygame.locals import *


class imagedisplay(pygame.sprite.Sprite):
    def __init__(self, pos, size, s_image):
        super(imagedisplay, self).__init__()
        self.surf = pygame.image.load("Sprites/" + s_image).convert()
        self.rect = self.surf.get_rect()
        self.rect.center = pos


class textdisplay(pygame.sprite.Sprite):
    def __init__(self, pos, text):
        super(textdisplay, self).__init__()
        self.font = pygame.font.Font(None, 36)
        self.surf = self.font.render(text, True, (10, 10, 10))
        self.rect = self.surf.get_rect()
        self.rect.center = pos

    def updatetext(self, newtext):
        self.surf = self.font.render(newtext, True, (10, 10, 10))
        pos = self.rect.center
        self.rect = self.surf.get_rect()
        self.rect.center = pos


def centeraround(images, pos, padding):
    currentx = -(len(images) * images[0].rect.width + (len(images) - 1) * padding) / 2.0 + pos[0]
    for image in images:
        image.rect.x = currentx
        image.rect.centery = pos[1]
        currentx += images[0].rect.width + padding


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption('PatternMaster2022')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    #first sprites
    playeractions = []
    playeractions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))
    playeractions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))
    playeractions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))
    playeractions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))
    playeractions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))
    playeractions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))
    playeractions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))

    centeraround(playeractions, (screen.get_size()[0]/2, screen.get_size()[1]/2), 20)

    spritelist = []
    spritelist.append(textdisplay((800, 800), "Banano"))
    for i in playeractions:
        spritelist.append(i)


    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            #print(event)
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                spritelist[0].updatetext("BANANA")
        background.fill((250, 250, 250))
        for sprite in spritelist:
            background.blit(sprite.surf, sprite.rect)


        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()


print(__name__)
