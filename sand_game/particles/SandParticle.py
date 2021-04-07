from sand_game.behaviours.FlammableBehaviour import FlammableBehaviour
from sand_game.particles.Particle import Particle
from sand_game.behaviours.FallBehaviour import FallBehaviour


class SandParticle(Particle):

    def __init__(self):
        super().__init__(10, "Sand", 0, 0, [FallBehaviour, FlammableBehaviour])
