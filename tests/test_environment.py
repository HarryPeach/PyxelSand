from sand_game.particles.SandParticle import SandParticle
from sand_game.Environment import Environment
from expects import expect, equal, be


class TestEnvironment():
    """Tests the Environment class
    """

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

    def test_env_set(self):
        """Test that the set function correctly sets the particle in a
        specific location
        """
        env = Environment(4, 4)

        bp = SandParticle()

        env.set(1, 1, bp)
        env.set(2, 2, bp)

        expect(env.env[10]).to(be(bp))
        expect(env.env[5]).to(be(bp))
