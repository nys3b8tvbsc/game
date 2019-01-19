from unit import Unit


class Animal(Unit):
    """Player`s pet."""

    def __init__(self, level: int, image: str):
        Unit.__init__(level, image)
