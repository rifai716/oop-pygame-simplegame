import pygame

class Enemy:
  def __init__(self, screen, resolution, position=[0, 0], speed=2):
    self.screen = screen
    self.resolution = resolution
    self.position = position
    self.speed = speed
    self.rect = None
    self.setup()
    self.step = 0
    
  def setup(self):
    pass
    
  def tiles(self):
    pass
    
  def hit_sound(self):
    pass
  
  def collision_with_bullet(self, enemies, bullet):
    pass
  
  def collision_with_player(self, enemies, player):
    pass
  
  def collision_with_castle(self, enemies):
    if self.position[0] <= 64:
      self.hit_sound()
      enemies.remove(self)
  
  def draw(self):
    if self.step >= 6:
      self.step = 0
    self.rect = pygame.Rect(self.tiles()[self.step//3].get_rect())
    self.rect.top = self.position[1]
    self.rect.left = self.position[0]
    self.position[0] -= self.speed
    self.screen.blit(self.tiles()[self.step//3], self.position)
    self.step += 1
  