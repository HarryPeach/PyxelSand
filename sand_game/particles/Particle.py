from abc import ABC, abstractmethod
from sand_game.behaviours.Behaviour import Behaviour


class Particle(ABC):
    """Represents a single particle, should be extended for any custom
    particles
    """

    @abstractmethod
    def __init__(self, color: int, name: str,
                 x: int, y: int, behaviours: list[Behaviour]):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.behaviours = behaviours
