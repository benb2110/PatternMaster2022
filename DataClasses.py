import pygame
from pygame.locals import *


class character():
    def __init__(self, max_hp):
        self.action_queue = []
        self.hp = max_hp
        self.max_hp = max_hp


class action:
    def __init__(self, action_list):
        action_list.append(self)
        self.damage_dict = {}
        self.flub_list = []
