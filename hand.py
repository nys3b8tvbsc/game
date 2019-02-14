import pygame

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
        self._cards.extend(cards)
        self.positioning()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.click(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            self.hover(event.pos)

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
                return 0

    def __len__(self):
        return len(self._cards)


def hand_create(deck, screen_size, height):
    cards = deck.return_cards(MAX_HAND, height)
    return Hand(screen_size, cards)
