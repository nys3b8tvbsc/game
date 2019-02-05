from const.hand import MAX_HAND


class Hand:
    def __init__(self, screen_size, cards):
        self._cards = cards
        self._width = screen_size[0]
        self._height = cards[0].rect.height
        self._y = screen_size[1] - self._height
        self._card_width = cards[0].rect.width
        self.positioning()
        self._selected_card = None

    def positioning(self):
        width = int(self._width / len(self._cards))
        start_position = int(width / 2 - self._card_width / 2)
        if start_position < 0:
            start_position = 0

        for i, card in enumerate(self._cards):
            card.move_to(start_position + i * width, self._y)

    def blit_me(self, surface):
        for card in self._cards:
            card.blit_me(surface)

    def append(self, cards):
        for card in cards:
            self._cards.append(card)
        self.positioning()

    def hover(self, xy):
        for card in self._cards:
            card.defocus()
        for card in reversed(self._cards):
            if card.rect.collidepoint(xy):
                card.focus()
                return

    def click(self, xy):
        for card in reversed(self._cards):
            if card.rect.collidepoint(xy):
                card.click()
                self._selected_card = card
                break
        for card in self._cards:
            if card is not self._selected_card:
                card.deselect()

    def delete_active(self):
        for card in self._cards.copy():
            if card is self._selected_card:
                self._cards.remove(card)
                self.positioning()
                self._selected_card = None
                return 0  # ?

    def __len__(self):
        return len(self._cards)


def hand_create(deck, screen_size, height):
    cards = deck.return_cards(MAX_HAND, height)
    return Hand(screen_size, cards)


"""
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1500, 1000))
cards=[]
with open('config/cards/fire_card1.json', 'r', encoding='utf-8') as fh:
    c1=create_card((0,0),500,json.load(fh))
with open('config/cards/sword_card1.json', 'r', encoding='utf-8') as fh:
    c2=create_card((0,0),500,json.load(fh))
with open('config/cards/fire_card1.json', 'r', encoding='utf-8') as fh:
    c3=create_card((0,0),500,json.load(fh))
cards.append(c1)
cards.append(c2)
cards.append(c3)
h1=Hand((1500,1000),cards)
screen.fill(WHITE)
h1.blit_me(screen)
pygame.display.update()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            with open('config/cards/fire_card1.json', 'r', encoding='utf-8') as fh:
                h1.app_card(json.load(fh))
        elif event.type==pygame.MOUSEBUTTONDOWN:
            h1.click(pygame.mouse.get_pos())
    h1.hover(pygame.mouse.get_pos())
    screen.fill(WHITE)
    h1.blit_me(screen)
    pygame.display.update()
"""
