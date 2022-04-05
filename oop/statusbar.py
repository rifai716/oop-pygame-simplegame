import pygame

class Health:
  def __init__(self, screen, inittial):
    self.value = inittial
  
  def increase(self, v):
    self.value += v
  
  def decrease(self, v):
    self.value -= v
    
  def track_mask(self):
    return pygame.image.load("../resources/images/healthbar.png")
  
  def thumb_mask(self):
    return pygame.image.load("../resources/images/health.png")
    