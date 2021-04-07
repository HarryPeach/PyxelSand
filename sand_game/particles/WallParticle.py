from sand_game.particles.Particle import Particle
from sand_game.behaviours.FallBehaviour import FallBehaviour


class WallParticle(Particle):

    def __init__(self):
        super().__init__(13, False, "Wall", 0, 0, [])
