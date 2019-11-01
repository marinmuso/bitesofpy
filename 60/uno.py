import itertools
from collections import namedtuple


SUITS = 'Red Green Yellow Blue'.split()
UnoCard = namedtuple('UnoCard', 'suit name')

def card_lists():
   vals = []
   num_values = [str(0)] + [str(num) for num in range(1, 10)] * 2
   draw_two = ['Draw Two'] * 2
   skip = ['Skip'] * 2
   reverse = ['Reverse'] * 2
   wild = ['Wild'] * 4
   wild_draw = ['Wild Draw Four'] * 4
   vals += num_values + draw_two + skip + reverse
   return vals, wild, wild_draw

def create_uno_deck():
   deck = []
   vals, wild, wild_draw = card_lists()
   [deck.append(UnoCard(suit, name)) for suit, name in itertools.product(SUITS, vals)]
   [deck.append(UnoCard(None, name)) for name in wild]
   [deck.append(UnoCard(None, name)) for name in wild_draw]
   return deck
