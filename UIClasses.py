import pygame
from pygame.locals import *



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
