# PyxelSand

> PyxelSand is a "falling sand" style game written with the Python game engine [Pyxel](https://github.com/kitao/pyxel)

![An example of the game running](https://i.imgur.com/d7AUAQM.gif)

## How to install

1. Install [Poetry](https://python-poetry.org/)
2. Run `poetry install` in the root directory
3. Run `poetry run python -m sand_game`

## How to play
- Left click places a particle at the mouses location
- Right click removes a particle at the mouses location
- Keys 1-3 select the implemented particles

## How it works
The game has an "environment" which keeps the state of each pixel and what particle is in it. Each particle extends from a base particle class, and upon initialization provides a list of behaviours such as "Flammable", "Fall", and "Ephemeral" to define how the particle behaves.