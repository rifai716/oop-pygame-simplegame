import pygame
from oop.enemy import Enemy

class Mouse(Enemy):
  
  speed = 5
  
  def setup(self):
    self.speed = Mouse.speed
  
  def tiles(self):
    return [
      pygame.image.load('resources/images/badguy.png'),
      pygame.image.load('resources/images/badguy2.png'),
      pygame.image.load('resources/images/badguy3.png'),
      pygame.image.load('resources/images/badguy4.png'),
    ]
  
  def hit_sound(self):
    tmp = pygame.mixer.Sound("resources/audio/enemy.wav")
    tmp.set_volume(0.05)
    tmp.play()