import pygame
from pygame.locals import *


class imagedisplay(pygame.sprite.Sprite):
    def __init__(self, pos, size, s_image):
        super(imagedisplay, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/" + s_image).convert(), size)
        self.rect = self.surf.get_rect()
        self.rect.center = pos

    def updateimage(self, newimage):
        pos = self.rect.center
        size = self.rect.size
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/" + newimage).convert(), size)
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


class Button:
    def __init__(self, pos, size, text):
        self.background = imagedisplay(pos, size, "Button.png")
        self.text = textdisplay(pos, text)

    def button_check_click(self, pos):
        if self.background.rect.collidepoint(pos[0], pos[1]):
            self.action()



    def add_to_render(self, spritelist):
        spritelist.append(self.background)
        spritelist.append(self.text)



def centeraround(images, pos, padding):
    currentx = -(len(images) * images[0].rect.width + (len(images) - 1) * padding) / 2.0 + pos[0]
    for image in images:
        image.rect.x = currentx
        image.rect.centery = pos[1]
        currentx += images[0].rect.width + padding


def testaction():
    print("Success!!")





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
    for i in range(7):
        playeractions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))

    enemyactions = []
    for i in range(7):
        enemyactions.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))


    playerchoices = []
    for i in range(6):
        playerchoices.append(imagedisplay((0, 0), (100, 100), "Warrior.png"))


    playerhp = textdisplay((180, 800), "Player HP: " + "100")
    enemyhp = textdisplay((1400, 800), "Enemy HP: " + "100")
    enemyname = textdisplay((1355, 765), "Gregore")
    playerimage = imagedisplay((180, 680), (200, 200), "Warrior.png")
    enemyimage = imagedisplay((1400, 680), (200, 200), "Warrior.png")

    centeraround(playeractions, (screen.get_size()[0]/2, 600), 20)
    centeraround(playerchoices, (screen.get_size()[0]/2, 800), 20)
    centeraround(enemyactions, (screen.get_size()[0]/2, 400), 20)

    spritelist = []
    spritelist.append(playerhp)
    spritelist.append(enemyhp)
    spritelist.append(enemyname)
    spritelist.append(playerimage)
    spritelist.append(enemyimage)


    for i in playeractions:
        spritelist.append(i)
    for i in enemyactions:
        spritelist.append(i)
    for i in playerchoices:
        spritelist.append(i)

    buttonlist = []
    nextturn = Button((500, 500), (150, 40), "Next turn")
    buttonlist.append(nextturn)
    nextturn.add_to_render(spritelist)
    nextturn.action = testaction

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
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                for button in buttonlist:
                    button.button_check_click(mousepos)

            if event.type == KEYDOWN and event.key == K_h:
                playerimage.updateimage("WarriorHat.png")
        background.fill((250, 250, 250))
        for sprite in spritelist:
            background.blit(sprite.surf, sprite.rect)


        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()


print(__name__)
