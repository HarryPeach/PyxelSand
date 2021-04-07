

from sand_game.Environment import Environment
from sand_game.behaviours.Behaviour import Behaviour


class FallBehaviour(Behaviour):
    def behave(env: Environment, loc: tuple[int, int]) -> tuple[int, int]:
        if (loc[1] + 1) >= env.height:
            return (loc[0], loc[1])

        particle_below = env.get(loc[0], loc[1] + 1)
        particle = env.get(loc[0], loc[1])

        if particle_below is None:
            env.set(loc[0], loc[1] + 1, particle)
            env.set(loc[0], loc[1], None)
            return (loc[0], loc[1] + 1)

        return (loc[0], loc[1])
