from random import randint
import pygame

class Level:
    def __init__(self, screen, resolution):
        self.screen = screen
        self.resolution = resolution
        self.castle = None
        self.enemies = []
        self.weapons = []
        self.background_sound()
        self.setup()
        self.enemy_timer = 0

    def setup(self):
        pass

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_weapon(self, cordinate):
        self.weapons.append(cordinate)

    def background_sound(self, volume=0.25):
        pass

    def tiles(self):
        pass
    
    def play(self, player):
        self.player = player

    def draw(self):
        for x in range(int(self.resolution[0]/self.tiles().get_width()+1)):
            for y in range(int(self.resolution[1]/self.tiles().get_height()+1)):
                self.screen.blit(
                    self.tiles(), (x*self.tiles().get_width(), y*self.tiles().get_height()))

        self.castle.draw()
        
        self.enemy_timer -= 1
        if self.enemy_timer <= 0:
            self.add_enemy(self.enemy[randint(0, len(self.enemy)-1)](
                self.screen, self.resolution, [self.resolution[0], randint(50, self.resolution[1]-32)]))
            self.enemy_timer = randint(1, 100)

        index = 0
        for enemy in self.enemies:
            enemy.collision_with_castle(self.enemies)
            for b in self.player.weapon.bullets:
              bullet_rect = pygame.Rect(self.player.weapon.tiles().get_rect())
              bullet_rect.left = b[1]
              bullet_rect.top = b[2]
              #print(bullet_rect.top)
              #print(pygame.Rect(enemy.tiles()[0].get_rect()).colliderect(bullet_rect))
              if enemy.tiles()[0].get_rect().colliderect(bullet_rect):
                print('menyerang', index)                

            index += 1
        
        for enemy in self.enemies:
            enemy.draw()
        
        # print('Total bulet yang keluar : ', len(self.player.weapon.bullets))
                
