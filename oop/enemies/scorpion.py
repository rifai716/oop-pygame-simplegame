import pygame
from oop.enemy import Enemy

class Scorpion(Enemy):
  
  speed = 2
  
  def setup(self):
    self.speed = Scorpion.speed
  
  def tiles(self):
    return [
      pygame.image.load('resources/images/scorpion.png'),
      pygame.image.load('resources/images/scorpion.png'),
      pygame.image.load('resources/images/scorpion.png'),
      pygame.image.load('resources/images/scorpion.png')
    ]
  
  def hit_sound(self):
    tmp = pygame.mixer.Sound("resources/audio/enemy.wav")
    tmp.set_volume(0.05)
    tmp.play()