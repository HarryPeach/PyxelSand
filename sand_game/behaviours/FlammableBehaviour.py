

from sand_game.particles.FireParticle import FireParticle
from sand_game.Environment import Environment
from sand_game.behaviours.Behaviour import Behaviour


class FlammableBehaviour(Behaviour):
    def behave(env: Environment, loc: tuple[int, int]) -> tuple[int, int]:
        left_particle = env.get(loc[0] - 1, loc[1])
        right_particle = env.get(loc[0] + 1, loc[1])
        up_particle = env.get(loc[0], loc[1] - 1)
        down_particle = env.get(loc[0], loc[1] + 1)

        if left_particle is not None:
            if isinstance(left_particle, FireParticle):
                env.set(loc[0], loc[1], FireParticle())

        if right_particle is not None:
            if isinstance(right_particle, FireParticle):
                env.set(loc[0], loc[1], FireParticle())

        if up_particle is not None:
            if isinstance(up_particle, FireParticle):
                env.set(loc[0], loc[1], FireParticle())

        if down_particle is not None:
            if isinstance(down_particle, FireParticle):
                env.set(loc[0], loc[1], FireParticle())
