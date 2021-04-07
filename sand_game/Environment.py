from typing import Union
from sand_game.particles.Particle import Particle


class Environment():
    """The 'Environment' of the simulation, maintains the state of each pixel
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.env = [None] * width * height

    def set(self, x: int, y: int, particle: Union[Particle, None]) -> None:
        """Sets the particle at the current location

        Args:
            x (int): The x-coordinate
            y (int): The y-coordinate
            particle (Particle | None): The particle to set, or None
        """
        if x > self.width or x < 0:
            return
        if y > self.height - 1 or y < 0:
            return
        self.env[(x % self.width) + (y * self.width)] = particle

    def get(self, x: int, y: int) -> Union[Particle, None]:
        """Get the particle at the current location

        Args:
            x (int): The x-coordinate
            y (int): The y-coordinate

        Returns:
            Particle | None: The particle at the location, or None
        """
        if x > self.width or x < 0:
            return None
        if y > self.height - 1 or y < 0:
            return None
        return self.env[(x % self.width) + (y * self.width)]
