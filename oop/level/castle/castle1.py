import pygame
from oop.statusbar import Health

class Castle:
  def __init__(self, screen):
    self.screen = screen
    self.health = Health(screen, 200)
  
  def tiles(self):
    return pygame.image.load('resources/images/castle.png')
  
  def hit_sound(self):
    tmp = pygame.mixer.Sound("resources/audio/explode.wav")
    tmp.set_volume(0.05)
    return tmp
  
  def draw(self):
    self.screen.blit(self.tiles(), (0, 30))
    self.screen.blit(self.tiles(), (0, 135))
    self.screen.blit(self.tiles(), (0, 240))
    self.screen.blit(self.tiles(), (0, 345))