import pygame

class Player:

    def __init__(self, screen):
        self.screen = screen
        self.position = [100, 100]
        self.static_position = (100, 100)
        self.angle = 0
        self.speed = 10

    def tiles(self):
        tmp = pygame.image.load('resources/images/dude.png')
        return pygame.transform.rotate(tmp, 360 - self.angle * 57.29)

    def rotate(self, angle):
        self.angle = angle

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def set_weapon(self, weapon):
        weapon.set_screen(self.screen)
        self.weapon = weapon

    def shoot(self):
        self.weapon.add_bullet(
            [self.angle, self.static_position[0]+32, self.static_position[1]+32])

    def draw(self):
        self.static_position = (self.position[0] - self.tiles().get_rect(
        ).width/2, self.position[1] - self.tiles().get_rect().height/2)
        self.screen.blit(self.tiles(), self.static_position)
        self.weapon.draw()
