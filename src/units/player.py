from unit import Unit


class Player(Unit):
    def __init__(self, cards, img_path: str):
        super().__init__(level=1, img_path=img_path)
        self.cards = cards

    def take_damage(self, damage: int):
        pass
