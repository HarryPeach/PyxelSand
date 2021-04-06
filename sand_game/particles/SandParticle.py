from pyxel import play
from sand_game.particles.BaseParticle import BaseParticle


class SandParticle(BaseParticle):

    def __init__(self, x: int, y: int):
        self.color = 10
        self.kinematic = True
        self.x = x
        self.y = y

    def update(self):
        super().update()
