import pygame


class Player:

    def __init__(self, scene, weapon):
        self.scene = scene
        self.screen = scene.screen
        self.position = [100, 100]
        self.static_position = (100, 100)
        self.angle = 0
        self.speed = 10
        self.step = 0
        self.set_weapon(weapon)
        self.scene.interaction(self)

    def tiles(self):
        tmp = [
            pygame.image.load('resources/images/dude.png'),
            pygame.image.load('resources/images/dude2.png'),
        ]
        return pygame.transform.rotate(tmp[self.step//6], 360 - self.angle * 57.29)

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

    def move(self):
        self.step += 1
        if self.step >= 12:
            self.step = 0
        self.static_position = (self.position[0] - self.tiles().get_rect(
        ).width/2, self.position[1] - self.tiles().get_rect().height/2)

    def draw(self):
        self.move()
        self.screen.blit(self.tiles(), self.static_position)
        self.weapon.draw()
        # pygame.display.update() 
