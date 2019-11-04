WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
   for i in range(size):
      if i % 2 == 0:
         print((WHITE + BLACK) * (size // 2))
      else:
         print((BLACK + WHITE) * (size // 2))
