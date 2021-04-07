from sand_game.particles.SandParticle import SandParticle
from sand_game.Environment import Environment
from expects import expect, equal, be


class TestEnvironment():
    def test_env_creation(self):
        """Tests that an environment is successfully created
        """
        env = Environment(10, 10)

        expect(len(env.env)).to(equal(10 * 10))

        for item in env.env:
            expect(item).to(be(None))

    def test_env_get(self):
        """Test that the get function correctly returns the particle in a
        specific location
        """
        env = Environment(3, 3)

        bp = SandParticle()

        env.env[4] = bp
        env.env[7] = bp

        expect(env.get(1, 1)).to(be(bp))
        expect(env.get(1, 2)).to(be(bp))
