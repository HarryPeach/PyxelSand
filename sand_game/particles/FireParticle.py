from sand_game.particles.Particle import Particle
from sand_game.behaviours.EphemeralBehaviour import EphemeralBehaviour


class FireParticle(Particle):

    def __init__(self):
        super().__init__(9, "Fire", 0, 0, [EphemeralBehaviour])
