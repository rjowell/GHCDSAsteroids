'''
Create a file called "ship.py"
import pygame and random to the file
inside the file declare a class called "Ship" and define an init method that takes a single 'position' parameter

'''



import pygame, random


class Ship(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        #Pulls raw image file into game
        self.image = pygame.image.load('ship.png')
        #Scales image down to appropriate size
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        #Rotates Sprite
        self.image = pygame.transform.rotate(self.image, -90)
        #Creates a rectangular area around the sprite.
        self.rect = self.image.get_rect()
        #set the center of the sprite
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.speed)

    def checkReset(self, endPos):
        return self.rect.center[0] > endPos

    def reset(self, pos):
        self.rect.center = pos