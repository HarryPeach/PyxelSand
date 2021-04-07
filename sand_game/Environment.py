from typing import Union
from sand_game.particles.Particle import Particle


class Environment():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.env = [None] * width * height

    def set(self, x: int, y: int, particle: Union[Particle, None]) -> None:
        self.env[(x % self.width) + (y * self.width)] = particle

    def get(self, x: int, y: int) -> Particle:
        return self.env[(x % self.width) + (y * self.width)]

    # def get(self, i) -> Particle:
    #     return self.env[i]
