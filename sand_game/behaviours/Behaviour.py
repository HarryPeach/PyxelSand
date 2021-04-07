from abc import ABC, abstractmethod


class Behaviour(ABC):
    """Controls what a particle will do from one frame until the next
    """

    @abstractmethod
    def behave(env: "Environment", loc: tuple[int, int]) -> tuple[int, int]:
        """Called when the particle is updated, should return the new location
        of the particle if it was moved
        """
        pass
