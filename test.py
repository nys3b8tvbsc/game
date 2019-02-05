import sys

from enemy import *
from gang import Gang
from hand import *
from loading import load_deck, load_hero, load_enemy
from scene import *
from unit import *
from const.event import ENEMY_TOUCH

QUIT = pygame.USEREVENT
ADD_EXP = pygame.USEREVENT + 1

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
deck = Deck(load_deck('deck1.json'))
print((screen.get_width(), screen.get_height()))
screen.fill(WHITE)
enemies = []
enemies.append(create_enemy(load_enemy('enemy1.json')))
h1 = hand_create(deck, (screen.get_width(), screen.get_height()), 450)
enemies[0]._rect.y = 30
g1 = Gang(enemies)
g1.blit_me(screen)
p1 = create_hero(load_hero('hero1.json'))
print(p1.new_level)
pygame.display.update()
print(p1.exp)
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            g1.click(pygame.mouse.get_pos())
            h1.click(pygame.mouse.get_pos())
        elif event.type == ENEMY_TOUCH:
            p1.attack(g1._enemies[g1._active], h1._selected_card)
            print(p1._mana)
            h1.delete_active()
            h1.append(deck.return_cards(6 - len(h1), 450))
            g1.dead()
    screen.fill(WHITE)
    g1.blit_me(screen)
    h1.blit_me(screen)
    g1.animated()
    pygame.display.update()
