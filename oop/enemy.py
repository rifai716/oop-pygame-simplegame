import pygame

class Enemy:
  def __init__(self, screen, position=[0, 0], speed=2):
    self.screen = screen
    self.position = position
    self.speed = speed
    
  def tiles(self):
    pass
    
  def hit_sound(self):
    pass
  
  def collation_with_bullet(self):
    pass
  
  def collation_with_player(self):
    pass
  