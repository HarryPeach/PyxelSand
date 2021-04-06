from sand_game.particles.SandParticle import SandParticle
import pyxel
# from sand_game.PlaySpace import PlaySpace


class SandGame():

    def __init__(self, width: int, height: int) -> None:
        pyxel.init(width, height)
        pyxel.mouse(True)
        self.width = width
        self.height = height
        self.particles = [SandParticle(10, 10)]

        pyxel.run(self.draw, self.update)

    def draw(self) -> None:
        pyxel.cls(0)

        for particle in self.particles:
            pyxel.rect(particle.x, particle.y, 1, 1, particle.color)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):  # TODO: Check if space is taken
            self.particles.append(SandParticle(
                pyxel.mouse_x, pyxel.mouse_y))

        for particle in self.particles:
            particle.update()

            # Remove a particle if it goes off-screen
            if particle.y > self.height or particle.x > self.width:
                self.particles.remove(particle)


if __name__ == "__main__":
    SandGame(160, 120)
