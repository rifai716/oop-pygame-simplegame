import pygame


class Scene:
    def __init__(self, resolution):
        self.resolution = resolution  # (width, height)
        self.screen = pygame.display.set_mode(self.resolution)  # (screen pygame)
        self.level = 1
        self.levels = []

    def win_screen(self):
        return pygame.image.load("resources/images/youwin.png")

    def game_over_screen(self):
        return pygame.image.load("resources/images/gameover.png")

    def setup_level(self, *args):
        for i in args:
            i.setup(self.screen, self.resolution)
            self.levels.append(i)

    def next_level(self):
        self.level += 1

    def prev_level(self):
        self.level -= 1
        
    def fill(self):
        self.screen.fill(0)
        self.levels[self.level-1].draw()
