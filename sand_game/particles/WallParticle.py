from sand_game.particles.Particle import Particle
from sand_game.behaviours.FallBehaviour import FallBehaviour


class WallParticle(Particle):
    """A particle representing a wall, will not fall or burn
    """

    def __init__(self):
        super().__init__(13, "Wall", 0, 0, [])
