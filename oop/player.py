import pygame


class Player:

    def __init__(self, scene, weapon):
        self.scene = scene
        self.screen = scene.screen
        self.position = [100, 100]
        self.angle = 0
        self.speed = 3
        self.step = 0
        self.set_weapon(weapon)
        self.scene.interaction(self)
        self.sprites = self.get_sprites()
        # self.sprites[0].fill((255,5,10))
        # self.sprites[1].fill((25,5,10))
        self.rect = self.sprites[0].get_rect()
        self.rect.midbottom = (self.position[0], self.position[1])

    def tiles(self):
        tmp = self.sprites
        return pygame.transform.rotate(tmp[self.step//6], 360 - self.angle * 57.29)
    
    def get_sprites(self):
        return [
            pygame.image.load('resources/images/dude.png'),
            pygame.image.load('resources/images/dude2.png'),
        ]

    def rotate(self, angle):
        self.angle = angle

    def move_up(self):
        self.position[1] -= self.speed
        self.rect.midbottom = self.position
        self.move()

    def move_down(self):
        self.position[1] += self.speed
        self.rect.midbottom = self.position
        self.move()

    def move_right(self):
        self.position[0] += self.speed
        self.rect.midbottom = self.position
        self.move()

    def move_left(self):
        self.position[0] -= self.speed
        self.rect.midbottom = self.position
        self.move()

    def set_weapon(self, weapon):
        weapon.set_screen(self.screen)
        self.weapon = weapon

    def shoot(self):
        self.weapon.add_bullet([self.angle, self.position[0], self.position[1]])

    def move(self):
        self.step += 1
        if self.step >= 12:
            self.step = 0
        
        if self.rect.midbottom[0] > self.scene.resolution[0]:
          self.position[0] = 0
        
        if self.rect.midbottom[1] > self.scene.resolution[1]:
          self.position[1] = 0
          
        if self.rect.midbottom[0] < 0:
          self.position[0] = self.scene.resolution[0]
        
        if self.rect.midbottom[1] < 0 :
          self.position[1] = self.scene.resolution[1]
        
    def draw(self):
        self.screen.blit(self.tiles(), self.rect)
        self.weapon.draw()
        pygame.display.update() 
