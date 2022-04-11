import pygame
from oop.level import Level
from oop.levels.castle.castle1 import Castle


class Level4(Level):
    ''' Level 4 - berlatar belakang rerumputan '''

    def setup_castle(self):
        self.castle = Castle(self.screen)

    def background_sound(self, volume=0.25):
        pygame.mixer.init()
        pygame.mixer.music.load("resources/audio/moonlight.wav")
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(volume)

    def tiles(self):
        return pygame.image.load('resources/images/grass.png')

    def draw(self):
        for x in range(int(self.resolution[0]/self.tiles().get_width()+1)):
            for y in range(int(self.resolution[1]/self.tiles().get_height()+1)):
                self.screen.blit(
                    self.tiles(), (x*self.tiles().get_width(), y*self.tiles().get_height()))

        self.castle.draw()
