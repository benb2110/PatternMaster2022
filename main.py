import pygame
from pygame.locals import *
from functools import partial

action_queue = []
enemy_action_queue = [3, 0, 0, 3, 0, 0, 0]
playeractions = []
enemyactions = []
buttonlist = []
spritelist = []
action_names = ["Quick Attack", "Normal Attack", "Heavy Attack", "Dodge", "Block", "Parry", "Heal"]
revealed_attacks = []
enemy = None
player_reveals = 2


colour_images = ["Green.png", "Blue.png", "Red.png", "Green.png", "Blue.png", "Red.png"]
shape_images = ["Circle.png", "Circle.png", "Circle.png", "Triangle.png", "Triangle.png", "Triangle.png"]
icons = ["Quick Attack.png", "Normal Attack.png", "Heavy Attack.png", "Dodge.png", "Parry.png", "Block.png"]




class imagedisplay(pygame.sprite.Sprite):
    def __init__(self, pos, size, s_image):
        super(imagedisplay, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/" + s_image).convert_alpha(), size)
        self.rect = self.surf.get_rect()
        self.rect.center = pos

    def updateimage(self, newimage):
        pos = self.rect.center
        size = self.rect.size
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/" + newimage).convert_alpha(), size)
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


class actiondisplay():
    def __init__(self, pos, size):
        self.background = imagedisplay(pos, size, "Button.png")
        reducedsize = (size[0]-8, size[1]-8)
        self.colourlayer = imagedisplay(pos, reducedsize, "Grey.png")
        self.shapelayer = imagedisplay(pos, reducedsize, "Blank.png")
        self.iconlayer = imagedisplay(pos, reducedsize, "Blank.png")
        self.rect = self.background.rect


    def button_check_click(self, pos):
        if hasattr(self, 'action') and self.rect.collidepoint(pos[0], pos[1]):
            self.action()

    def updateposition(self):
        self.background.rect = self.rect
        smallrect = Rect(self.rect.left + 4, self.rect.top + 4, self.rect.width - 8, self.rect.height -8)
        self.colourlayer.rect = smallrect
        self.shapelayer.rect = smallrect
        self.iconlayer.rect = smallrect

    def updateimages(self, colour, shape, icon):
        self.colourlayer.updateimage(colour)
        self.shapelayer.updateimage(shape)
        self.iconlayer.updateimage(icon)


    def add_to_render(self, spritelist):
        spritelist.append(self.background)
        spritelist.append(self.colourlayer)
        spritelist.append(self.shapelayer)
        spritelist.append(self.iconlayer)


def centeraround(images, pos, padding):
    currentx = -(len(images) * images[0].rect.width + (len(images) - 1) * padding) / 2.0 + pos[0]
    for image in images:
        image.rect.x = currentx
        image.rect.centery = pos[1]
        currentx += images[0].rect.width + padding


class character():
    def __init__(self, max_hp):
        self.action_queue = []
        self.hp = max_hp
        self.max_hp = max_hp



def testaction():
    print("Success!!")


def update_player_action_display():
    for i in range(len(playeractions)):
        if i < len(action_queue):
            playeractions[i].updateimages(colour_images[action_queue[i]], shape_images[action_queue[i]], icons[action_queue[i]])
        else:
            playeractions[i].updateimages("Grey.png", "Blank.png", "Blank.png")



def  update_enemy_action_display():
    for i in range(len(playeractions)):
        if revealed_attacks[i]:
            enemyactions[i].updateimages(colour_images[enemy.action_queue[i]], shape_images[enemy.action_queue[i]], icons[enemy.action_queue[i]])
        else:
            enemyactions[i].updateimages("Grey.png", "Blank.png", "Questionmark.png")

def reveal_enemy_attack(index):
    global player_reveals
    if player_reveals > 0:
        revealed_attacks[index] = True
        player_reveals -= 1
        update_enemy_action_display()



def cancel_action(action_index):
    print(action_index)
    if action_index < len(action_queue):
        del action_queue[action_index]
        update_player_action_display()


def add_action_to_queue(chosen_action):
    action_queue.append(chosen_action)
    update_player_action_display()


def setup_enemy_fight():
    global enemy
    enemy = character(3)
    setup_round()


def setup_round():
    global enemy
    global revealed_attacks
    global player_reveals
    revealed_attacks = [True, False, False, False, False, False, False]
    enemy.action_queue = [3, 0, 0, 3, 0, 0, 0]
    player_reveals = 2
    update_enemy_action_display()



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

    for i in range(7):
        playeractions.append(actiondisplay((0, 0), (100, 100)))


    for i in range(7):
        enemyactions.append(actiondisplay((0, 0), (100, 100)))


    playerchoices = []
    for i in range(6):
        playerchoices.append(actiondisplay((0, 0), (100, 100)))




    playerhp = textdisplay((180, 800), "Player HP: " + "100")
    enemyhp = textdisplay((1400, 800), "Enemy HP: " + "100")
    enemyname = textdisplay((1355, 765), "Gregore")
    playerimage = imagedisplay((180, 680), (200, 200), "Warrior.png")
    enemyimage = imagedisplay((1400, 680), (200, 200), "GoblinBG.png")

    centeraround(playeractions, (screen.get_size()[0]/2, 600), 20)
    centeraround(playerchoices, (screen.get_size()[0]/2, 800), 20)
    centeraround(enemyactions, (screen.get_size()[0]/2, 400), 20)


    spritelist.append(playerhp)
    spritelist.append(enemyhp)
    spritelist.append(enemyname)
    spritelist.append(playerimage)
    spritelist.append(enemyimage)


    nextturn = Button((1450, 850), (150, 40), "Next turn")
    buttonlist.append(nextturn)

    nextturn.add_to_render(spritelist)
    nextturn.action = testaction

    for i in playeractions:
        i.updateposition()
        i.add_to_render(spritelist)
        i.action = partial(cancel_action, playeractions.index(i))
        buttonlist.append(i)


    for i in enemyactions:
        i.updateposition()
        i.add_to_render(spritelist)
        i.action = partial(reveal_enemy_attack, enemyactions.index(i))
        buttonlist.append(i)


    for i in playerchoices:
        i.updateposition()
        i.add_to_render(spritelist)
        i.action = partial(add_action_to_queue, playerchoices.index(i))
        index = playerchoices.index(i)
        i.updateimages(colour_images[index], shape_images[index], icons[index])
        buttonlist.append(i)


    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    setup_enemy_fight()

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



