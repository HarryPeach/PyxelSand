from sand_game.PlaySpace import PlaySpace
from expects import expect, equal


class TestPlaySpace():
    def test_initialized(self):
        """
        Tests that a playspace is correctly initialized
        """
        ps = PlaySpace(20, 20)
        for row in ps.raw:
            for item in row:
                expect(item).to(equal(None))
