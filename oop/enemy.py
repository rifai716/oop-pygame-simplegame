import pygame

class Enemy:
  def __init__(self, screen, resolution, position=[0, 0], speed=2):
    self.screen = screen
    self.resolution = resolution
    self.position = position
    self.speed = speed
    self.setup()
    
  def setup(self):
    pass
    
  def tiles(self):
    pass
    
  def hit_sound(self):
    pass
  
  def collation_with_bullet(self):
    pass
  
  def collation_with_player(self):
    pass
  
  def draw(self):
    self.position[0] -= self.speed
    self.screen.blit(self.tiles(), self.position)
  