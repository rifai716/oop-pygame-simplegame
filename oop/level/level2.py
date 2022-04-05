import pygame


class Level2():
    ''' Level 1 - berlatar belakang gurun pasir '''

    def setup(self, screen, resolution):
        print(resolution)
        self.screen = screen
        self.resolution = resolution

    def tiles(self):
        return pygame.image.load('resources/images/pasir.jpg')

    def draw(self):
        for x in range(int(self.resolution[0]/self.tiles().get_width()+1)):
            for y in range(int(self.resolution[1]/self.tiles().get_height()+1)):
                self.screen.blit(
                    self.tiles(), (x*self.tiles().get_width(), y*self.tiles().get_height()))
