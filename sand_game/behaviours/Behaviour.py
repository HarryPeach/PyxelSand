from abc import ABC, abstractmethod
# from sand_game.particles.Particle import Particle
# from sand_game.Environment import Environment


class Behaviour(ABC):

    @abstractmethod
    def behave(env: 'Environment', loc: tuple[int, int]) -> tuple[int, int]:
        pass
