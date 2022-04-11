import pygame
from oop.enemy import Enemy

class Mouse(Enemy):
  
  def __init__(self):
    Enemy.__init__(self)
  
  def tiles(self):
    return pygame.image.load('resources/images/badguy.png')
  
  def hit_sound(self):
    tmp = pygame.mixer.Sound("resources/audio/enemy.wav")
    tmp.set_volume(0.05)
    return tmp