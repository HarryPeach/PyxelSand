

from sand_game.Environment import Environment
from sand_game.behaviours.Behaviour import Behaviour


class EphemeralBehaviour(Behaviour):
    """Removes the particle after one frame
    """
    def behave(env: Environment, loc: tuple[int, int]) -> tuple[int, int]:
        env.set(loc[0], loc[1], None)
