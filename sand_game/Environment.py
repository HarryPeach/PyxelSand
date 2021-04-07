from typing import Union
from sand_game.particles.Particle import Particle


class Environment():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.env = [None] * width * height

    def set(self, x: int, y: int, particle: Union[Particle, None]) -> None:
        if x > self.width or x < 0:
            return
        if y > self.height - 1 or y < 0:
            return
        self.env[(x % self.width) + (y * self.width)] = particle

    def get(self, x: int, y: int) -> Particle:
        if x > self.width or x < 0:
            return None
        if y > self.height - 1 or y < 0:
            return None
        return self.env[(x % self.width) + (y * self.width)]
