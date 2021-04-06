from abc import ABC, abstractmethod


class BaseParticle(ABC):

    @abstractmethod
    def __init__(self, color: int, kinematic: bool,
                 x: int, y: int):
        self.color = color
        self.kinematic = kinematic
        self.x = x
        self.y = y

    @abstractmethod
    def update(self):
        self.__update_gravity()

    def __update_gravity(self):
        """Updates the y-value of the particle according to gravity
        """
        if not self.kinematic:
            return

        self.y = self.y + 1
