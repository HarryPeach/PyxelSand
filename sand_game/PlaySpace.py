
class PlaySpace():

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.raw = [[None for _ in range(width)] for __ in range(height)]

    def push_particle(self, x: int, y: int, x_delta: int, y_delta: int):
        """Pushes the particle by a specific delta

        Args:
            x (int): The particles x value
            y (int): The particles y value
            x_delta (int): The x amount that the particle should move in
            y_delta (int): The y amount that the particle should move in
        """
        new_loc = self.raw[x + x_delta][y + y_delta]
        try:
            if new_loc is None:
                new_loc = self.raw[x][y]
                self.raw[x][y] = None
            else:
                raise ValueError()
        except IndexError:
            raise ValueError()
