from abc import ABC, abstractmethod
from sand_game.behaviours.Behaviour import Behaviour


class Particle(ABC):

    @abstractmethod
    def __init__(self, color: int, name: str,
                 x: int, y: int, behaviours: list[Behaviour]):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.behaviours = behaviours
