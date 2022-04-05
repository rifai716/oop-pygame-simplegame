import pygame
from oop.bullet import Arrow
from oop.control import GameController
from oop.scene import Scene
from oop.level.level1 import Level1
from oop.level.level2 import Level2
from oop.player import Player

pygame.init()

scene = Scene((640, 480))
scene.setup_level(
  Level1(),
  Level2()
)

player = Player(scene.screen)
player.set_weapon(Arrow())
game_controller = GameController(player)

running = True

while(running):
  scene.fill()
  game_controller.keyboard_event()
  game_controller.mouse_position_event()
  player.draw()
  pygame.display.flip()