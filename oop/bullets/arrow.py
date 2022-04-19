import pygame
from oop.bullet import Bullet


class Arrow(Bullet):
	max_bullet = 5000000000

	def __init__(self):
		Bullet.__init__(self, Arrow.max_bullet)
		self.sprites = self.get_sprites()
		self.sound = self.get_sound()

	def tiles(self):
		return self.sprites

	def get_sprites(self):
		return pygame.image.load('resources/images/bullet.png')

	def get_sound(self):
		return pygame.mixer.Sound("resources/audio/shoot.wav")

	def shoot_sound(self):
		tmp = self.sound
		tmp.set_volume(0.05)
		tmp.play()

	def hit_enemy_sound(self):
		pass

	def hit_enemy(self, enemies):
		pass
