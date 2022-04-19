import pygame
from oop.enemy import Enemy

class Scorpion(Enemy):
  
  speed = 0.5
  
  def setup(self):
    self.speed = Scorpion.speed
    self.sprites = self.get_sprites()
    self.sound = self.get_sound()
  
  def tiles(self):
    return self.sprites
  
  def get_sprites(self):
    return [
      pygame.image.load('resources/images/scorpion.png'),
      pygame.image.load('resources/images/scorpion.png'),
      pygame.image.load('resources/images/scorpion.png'),
      pygame.image.load('resources/images/scorpion.png')
    ]
    
  def get_sound(self):
    return pygame.mixer.Sound("resources/audio/enemy.wav")
  
  def hit_sound(self):
    tmp = self.sound
    tmp.set_volume(0.05)
    tmp.play()