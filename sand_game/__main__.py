import pyxel
from sand_game.Environment import Environment
from sand_game.particles.SandParticle import SandParticle
from sand_game.particles.WallParticle import WallParticle


class SandGame():

    def __init__(self, width: int, height: int) -> None:
        pyxel.init(width, height)
        pyxel.mouse(True)
        self.width = width
        self.height = height
        self.env = Environment(width, height)

        pyxel.run(self.draw, self.update)

    def draw(self) -> None:
        pyxel.cls(0)

        for x in range(self.width):
            for y in range(self.height):
                particle = self.env.get(x, y)
                if particle is None:
                    continue

                pyxel.rect(x, y, 1, 1, particle.color)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self.env.set(pyxel.mouse_x, pyxel.mouse_y, SandParticle())

        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            self.env.set(pyxel.mouse_x, pyxel.mouse_y, WallParticle())

        # Don't re-update particles that have moved
        updated_particles = []

        for x in range(self.width):
            for y in range(self.height):
                particle = self.env.get(x, y)
                if particle is None:
                    continue

                if particle in updated_particles:
                    continue

                for behaviour in particle.behaviours:
                    behaviour.behave(self.env, (x, y))
                updated_particles.append(particle)


if __name__ == "__main__":
    SandGame(160, 120)
