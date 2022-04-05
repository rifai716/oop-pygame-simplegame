import pygame

class Enemy:
  def __init__(self):
    self.position = [0, 0]
    self.speed = 2
    
  def mask(self):
    return pygame.image.load('resources/images/badguy.png')
    
  def hit_sound(self):
    tmp = pygame.mixer.Sound("resources/audio/enemy.wav")
    tmp.set_volume(0.05)
    return tmp