class Level:
    def __init__(self, screen, resolution):
        self.screen = screen
        self.resolution = resolution
        self.enemies = []
        self.weapons = []
        self.background_sound()
        self.setup_castle()
        
    def setup_castle(self):
        pass

    def add_enemy(self, cordinate):
        self.enemies.append(cordinate)

    def add_weapon(self, cordinate):
        self.weapons.append(cordinate)

    def background_sound(self, volume=0.25):
        pass

    def tiles(self):
        pass

    def draw(self):
        pass
