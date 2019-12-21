from pygame.locals import *
from GameSprite import GameSprite
from pygame import math as pymath
import pygame


class Player(object):
    def __init__(self, scene):
        self.scene = scene
        # Player status
        self.isDead = False
        # Media for player
        self.image = 'media/player.png'
        self.image_dead = 'media/player_dead.png'
        # Player dimensions
        self.dwidth = 100
        self.dheight = 75
        # Player direction
        self.direct_x = 0
        self.direct_y = 0
        # Pygame code generation
        self.rect = Rect(0, 0, self.dwidth, self.dheight)
        self.sprite = GameSprite(self.image)
        self.sprite_surface = self.sprite.getImage() # get player sprite surface
        # Player position
        self.pwidth = 660
        self.pheight = 660
        # Init player position
        self.pos = pymath.Vector2(self.pwidth / 2, self.pheight / 2)
        self.draw_pos = pymath.Vector2(self.pos.x, self.pos.y)
        # game window icon = self.sprite_surface
        pygame.display.set_icon(self.sprite_surface)

    def update(self):
        if self.direct_x == -0.1:
            if self.pos.x > 0:
                self.pos.x += self.direct_x
        elif self.direct_x == 0.1:
            if self.pos.x + self.dwidth <= self.pwidth:
                self.pos.x += self.direct_x
        if self.direct_y == -0.1:
            if self.pos.y > 0:
                self.pos.y += self.direct_y
        elif self.direct_y == 0.1:
            if self.pos.y + self.dheight <= self.pheight:
                self.pos.y += self.direct_y

        self.draw_pos = pymath.Vector2(self.pos.x, self.pos.y)

    def get_pos(self):
        return (self.pos.x, self.pos.y)

    def update_sprite(self):
        if self.isDead:
            self.sprite = GameSprite(self.image, self.rect)
        elif not self.isDead:
            self.sprite = GameSprite(self.image_dead, self.rect)

    def die(self):
        self.isDead = True
        self.update_sprite()

    def set_x(self, _x):

        # new direction x
        self.direct_x = _x

    def set_y(self, _y):

        # new direction y
        self.direct_y = _y

    def draw(self):
        self.scene.blit(self.sprite_surface, self.draw_pos)
