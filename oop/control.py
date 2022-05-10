import pygame
from pygame.locals import *
import math
import sys


class GameController:
    def __init__(self, player):
        self.player = player
        self.keys = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False,
            "shoot": False
        }

    def keyboard_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    self.keys["top"] = True
                elif event.key == K_a:
                    self.keys["left"] = True
                elif event.key == K_s:
                    self.keys["bottom"] = True
                elif event.key == K_d:
                    self.keys["right"] = True
            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    self.keys["top"] = False
                elif event.key == K_a:
                    self.keys["left"] = False
                elif event.key == K_s:
                    self.keys["bottom"] = False
                elif event.key == K_d:
                    self.keys["right"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.shoot()

        if self.keys["top"]:
            self.player.move_up()
        elif self.keys["bottom"]:
            self.player.move_down()
        if self.keys["left"]:
            self.player.move_left()
        elif self.keys["right"]:
            self.player.move_right()

    def mouse_position_event(self):
        mouse_position = pygame.mouse.get_pos()
        angle = math.atan2(mouse_position[1] - (self.player.position[1]+32),
                           mouse_position[0] - (self.player.position[0]+26))
        self.player.rotate(angle)
