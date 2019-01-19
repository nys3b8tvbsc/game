from unit import Unit


class Player(Unit):
    def __init__(self, cards, image: str):
        Unit.__init__(level=1, image=image)
        self.cards = cards

    def take_damage(self, damage: int):
        pass
